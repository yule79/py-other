import streamlit as st

st.title("SAVE-URL")

url=st.text_input(label="URLを入力")
name=st.text_input(label="サイト名を入力")


url_len=len(url)


if 'http' and '://' in url:
    if url_len>=10:
        if url and name:
            st.page_link(url, label=name)

            if st.button("URLを保存"):
                with open('url.txt','a',encoding='utf-8') as file:
                    file.write(name+'\n')
                    file.write(url+'\n')
                    file.write(" "+'\n')
                st.info("保存しました")