#
import streamlit as st


ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# text_input을 활용해서 검색창을 만듭니다.
# 이 검색창에 ani_list 일부 단어가 일치하면
# img_list의 해당 이미지를 출력하는 로직을 만들어 주세요
# if / for 를 활용하면 될 겁니다.

# 화면에 뜨는 것부터 1개만 만들고 
search_term = st.text_input("애니 검색")
if search_term:
    for i, ani in enumerate(ani_list):
        if search_term in ani:
            st.image(img_list[i], width=300)    # 이미지 인덱스와 애니 인덱스가 같은 내용이므로
            break
        else:
            st.write("검색어에 해당하는 애니가 없습니다.")  # write - > 매직 키워드 다 보여줌!
            break

else:
    st.write("검색어를 입력해 주세요.")


# 강사님 ver
# search = st.text_input('검색어를 입력하세요')
# if search != "":
#     for ani in ani_list:
#         if search in ani:
#             st.image(img_list[ani_list.index(ani)])
#             break