# New-operation-types-loader
Это программа для получения новых типов операций за неделю , или для получения всех типов операций

1. Для получения новых типов операций за последнюю неделю нужно использовать POST метод и запрос http://127.0.0.1:8000/api/v1/new_operation_types/
   a. Этот запрос делает запрос к апи валбериса, определяет новые типы операций и заносит их в базу данных
   b. И в конце он возвращает список всех новые типы операций за последнюю неделю

2. Для получения всех имеющихся типов операций нужно выполнить GET запрос http://127.0.0.1:8000/api/v1/all_operation_types/
   a. Этот запрос возвращает список всех уже имеюшихся типов операций 
