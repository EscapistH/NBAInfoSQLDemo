# encoding:utf-8

import control
import menu

menu.main_menu()

while True:
    # control.create_sql()
    switch = input('请输入你要进行的操作:')
    if switch == '1':  # add values
        playerId = input("please input a id to player:")
        playerName = input(r"请输入球员姓名:")
        playerTeam = input(r"请输入球员所在球队:")
        playerNumber = input(r"请输入球员球衣号码:")
        playerSeat = input(r"请输入球员擅长位置:")
        playerHeight = input(r"请输入球员身高:")
        control.insert_player(playerId, playerName, playerTeam, playerNumber, playerSeat, playerHeight)

    elif switch == '2':  # delete values
        playerName = input('请输入要删除的球员名字:')
        control.delete_player(playerName)

    elif switch == '3':  # change values
        playerName = input('请输入要修改的球员名字:')
        key = input('请选择要修改的数据:')
        menu.change_menu()
        if key == '1':
            newData = input('请输入新的数据')
            control.change_team(newData, playerName)
        elif key == '2':
            newData = input('请输入新的数据')
            control.change_number(newData, playerName)
        elif key == '3':
            newData = input('请输入新的数据')
            control.change_seat(newData, playerName)
        elif key == '4':
            newData = input('请输入新的数据')
            control.change_hight(newData, playerName)
        elif key == '0':
            break
        else:
            print('输入有误，请重新输入!')

    elif switch == '4':  # search values
        playerName = input("请输入要查询的球员姓名:")
        control.search_player(playerName)

    elif switch == '5':
        control.search_all()

    elif switch == '0':  # break loop(exit system)
        break

    else:
        print('输入有误,请重新输入!')
