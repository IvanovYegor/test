# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator=","):
    participants1 = set(participants_first_group.split(separator))
    participants2 = set(participants_second_group.split(separator))
    common_participants = participants1.intersection(participants2)
    return sorted(common_participants)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print("Общие участники:", common_participants)
# TODO Провеьте работу функции с разделителем отличным от запятой
