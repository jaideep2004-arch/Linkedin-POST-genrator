import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Page config
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="🚀",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-text {
        text-align: center;
        color: gray;
        margin-bottom: 25px;
    }
    .stButton>button {
        width: 100%;
        height: 50px;
        font-size: 18px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Options
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


def main():
    # Header
    st.markdown('<div class="main-title">🚀 LinkedIn Post Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text">Generate high-quality LinkedIn posts using AI</div>', unsafe_allow_html=True)

    # Load tags
    fs = FewShotPosts()
    tags = fs.get_tags()

    st.markdown("### 🔧 Customize your post")

    # Layout
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        selected_tag = st.selectbox("📌 Topic", options=tags)

    with col2:
        selected_length = st.selectbox("📏 Length", options=length_options)

    with col3:
        selected_language = st.selectbox("🌐 Language", options=language_options)



    st.markdown("---")

    # Generate Button
    if st.button("✨ Generate Post"):
        if not selected_tag:
            st.warning("⚠️ Please select a topic")
            return

        with st.spinner("🚀 Generating your post..."):
            try:
                # (tone not passed since backend unchanged)
                post = generate_post(selected_length, selected_language, selected_tag)

                st.success("✅ Post Generated Successfully!")

                # Output
                st.markdown("### 📝 Your Generated Post")
                st.text_area("", post, height=220)

                # Character count
                st.info(f"📊 Characters: {len(post)}")

                # Download button
                st.download_button(
                    label="📥 Download Post",
                    data=post,
                    file_name="linkedin_post.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"❌ Error: {e}")


if __name__ == "__main__":
    main()