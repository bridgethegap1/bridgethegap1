CREATE table accounts(
  "name" TEXT,
  "username" TEXT,
  "password" TEXT,
  "id" INT FOREIGN KEY
);

CREATE table posts(
  "message" TEXT,
  "username" TEXT
);
