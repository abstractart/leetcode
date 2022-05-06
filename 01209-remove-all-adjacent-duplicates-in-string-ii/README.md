# 1209. Remove All Adjacent Duplicates in String II

## Решение. через стэк (придумал сам)
Идем в цикле по строке, в стэке храним пары `(сhar, frequency)`
если `stack.top().char == curr_char` то. мы увеличиваем значение `frequency` в `stack.top().frequency += 1` и проверяем достигло ли значение `frequency` `k`
