
import streamlit as st
import requests

# Set up Streamlit app
st.title('Blog Generation App')

# User input for blog topic
blog_topic = st.text_input('Enter a blog topic:')

# Button to fetch data
if st.button('Generate Blog'):
    if blog_topic:
        # Define the API URL
        api_url = 'https://e53uqk4pw9.execute-api.us-east-1.amazonaws.com/dev/blog-generation'
        
        try:
            # Fetch data from the API
            response = requests.post(api_url, json={'blog_topic': blog_topic})
            response.raise_for_status()  # Raise an error for bad responses
            api_response = response.json()
            
            # Extract and display the blog content from the response
            blog_content = api_response.get('blog_content', 'No content returned')
            st.write('Generated Blog Content:')
            st.write(blog_content)
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error('Please enter a blog topic.')