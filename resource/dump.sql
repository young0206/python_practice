BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'KIM','kim@example.com','010-1234-5678','http://kim@example.com','2026-08-03 14:39:16');
INSERT INTO "users" VALUES(2,'Park','Park@daum.net','010-1111-2222','Park.com','2026-08-03 14:39:16');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-3333','Lee.com','2026-08-03 14:39:16');
INSERT INTO "users" VALUES(4,'Choi','Choi@gmail.com','010-3333-4444','Choi.com','2026-08-03 14:39:16');
INSERT INTO "users" VALUES(5,'Kim','Kim@daum.net','010-4444-5555','Kim.com','2026-08-03 14:39:16');
COMMIT;
