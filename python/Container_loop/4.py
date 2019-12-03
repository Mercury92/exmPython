input_id = input("아이디를 입력해주세요.\n")
# real_egoing = "11"
# real_k8805 = "ab"
members = ['egoing', 'k8805']


# if real_egoing == in_str:
#     print("Hello!, egoing")
# elif real_k8805 == in_str:
#     print("Hello!, k8805")
# else:
#     print("Who are you?")
for member in members:
    if member == input_id:
        print('hello!, ' + member)
        import sys
        sys.exit()

print('Who are you')
