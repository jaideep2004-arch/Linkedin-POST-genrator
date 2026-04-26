import json
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


# ✅ Clean text (fix Unicode issues)
def clean_text(text):
    return text.encode("utf-8", "ignore").decode("utf-8")


def process_posts(raw_file_path, processed_file_path=None):
    with open(raw_file_path, encoding='utf-8', errors='ignore') as file:
        posts = json.load(file)

    enriched_posts = []

    for post in posts:
        try:
            cleaned_text = clean_text(post.get('text', ''))
            metadata = extract_metadata(cleaned_text)

            post_with_metadata = {**post, **metadata}
            enriched_posts.append(post_with_metadata)

        except Exception as e:
            print(f"Error processing post: {e}")
            continue

    # ✅ unify tags
    unified_tags = get_unified_tags(enriched_posts)

    for post in enriched_posts:
        current_tags = post.get('tags', [])
        new_tags = [unified_tags.get(tag, tag) for tag in current_tags]
        post['tags'] = list(set(new_tags))

    # ✅ save output
    if processed_file_path:
        with open(processed_file_path, encoding='utf-8', mode="w", errors="ignore") as outfile:
            json.dump(enriched_posts, outfile, indent=4, ensure_ascii=False)

    print("✅ Processing complete!")


def extract_metadata(post):
    template = '''
    You are given a LinkedIn post. Extract:
    - line_count
    - language
    - tags

    Rules:
    1. Return ONLY valid JSON (no extra text)
    2. Keys must be: line_count, language, tags
    3. tags = array (max 2 tags)
    4. Language = English or Hinglish

    Post:
    {post}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke({"post": post})

    try:
        json_parser = JsonOutputParser()
        return json_parser.parse(response.content)
    except OutputParserException:
        print("⚠️ Failed to parse metadata")
        return {
            "line_count": 0,
            "language": "Unknown",
            "tags": []
        }


def get_unified_tags(posts_with_metadata):
    unique_tags = set()

    for post in posts_with_metadata:
        unique_tags.update(post.get('tags', []))

    tags_list = list(unique_tags)

    # ✅ FIXED TEMPLATE (escaped braces)
    template = '''
    You are given a list of tags.

    Your task:
    1. Merge similar tags into a single unified tag
    2. Use Title Case (e.g., "Job Search", "Motivation")
    3. Return ONLY JSON mapping like:
       {{"old_tag": "new_tag"}}

    Tags:
    {tags}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke({"tags": tags_list})

    try:
        json_parser = JsonOutputParser()
        return json_parser.parse(response.content)
    except OutputParserException:
        print("⚠️ Failed to unify tags")
        return {tag: tag for tag in tags_list}


if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")