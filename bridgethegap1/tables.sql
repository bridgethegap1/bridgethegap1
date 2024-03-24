CREATE table accounts(
  name TEXT;
  username TEXT;
  password TEXT;
  id int FOREIGN KEY;
);

CREATE table posts(
  message TEXT;
  username TEXT;
);
