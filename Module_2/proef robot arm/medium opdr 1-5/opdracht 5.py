# for _ in range(5):
#     while True:
#         if not robotArm.stackEmpty():
#             robotArm.grab()
#             break
#         elif robotArm.stackEmpty():
#             robotArm.moveRight()
#     for _ in range(9):
#         robotArm.moveRight()
#     while True:
#         if robotArm.stackEmpty():
#             robotArm.drop()
#             break
#         elif not robotArm.stackEmpty():
#             robotArm.moveLeft()
#     for _ in range(9):
#         robotArm.moveLeft()