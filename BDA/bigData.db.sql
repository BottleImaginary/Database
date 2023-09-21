BEGIN TRANSACTION;

CREATE TABLE user (
	"username"	VARCHAR(20) NOT NULL
);
CREATE TABLE botol (
	"gambar_botol"	BLOB NOT NULL,
	"waktu" SMALLDATETIME AFTER "gambar_botol"
);
COMMIT;