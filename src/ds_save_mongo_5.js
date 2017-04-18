use myDB #DB생성 (이미 존재하면 그대로 사용)
#아래에서 db는 지금 사용중인 myDB를 나타냄
db.myCol.insert({"Persons" : {"id":"405", "이름":"js1"}, {"id":"406", "이름":"js2"}})
#DB에 값 저장함

#찾아주는 과정
db.myCol.find({"Persons.이름":"js2"})