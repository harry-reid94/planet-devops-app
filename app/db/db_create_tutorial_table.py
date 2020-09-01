import sqlite3
conn = sqlite3.connect('testDB.db')


c = conn.cursor()




c.execute('''
		
CREATE TABLE tutorial_model (
  `id` INTEGER,
  `tag` VARCHAR(20) NULL DEFAULT NULL,
  `title` VARCHAR(100) NULL DEFAULT NULL,
  `content` INTEGER(2000) NULL DEFAULT NULL,

  PRIMARY KEY (`id`)
);

''')


conn.commit()