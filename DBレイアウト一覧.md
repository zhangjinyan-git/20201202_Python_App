# DBレイアウト一覧

#### TTPJM001 顧客マスター 

|  No  |   カラム名   |     カラムID     |    型    | 桁数 |  PK  | IDX1 | IDX2 | IDX3 | default | not null | 備考                                       |
| :--: | :----------: | :--------------: | :------: | :--: | :--: | :--: | :--: | :--: | :-----: | :------: | :----------------------------------------- |
|  1   |      ID      |        id        |   int    |  11  |  1   |      |      |      |         |          |                                            |
|  2   |   password   |    パスワード    | varchar  | 128  |      |      |      |      |         |    1     |                                            |
|  ３  |  last_login  | 最後ログイン日時 | datetime |      |      |      |      |      |         |          |                                            |
|  4   | is_superuser |   管理員フラグ   | tinyint  |  1   |      |      |      |      |         |    1     |                                            |
|  5   |   username   |    ユーザーID    | varchar  | 150  |      |  1   |      |      |         |    1     |                                            |
|  6   |  first_name  | ファーストネーム | varchar  | 150  |      |      |      |      |         |    1     |                                            |
|  7   |  last_name   |   ラストネーム   | varchar  | 150  |      |      |      |      |         |    1     |                                            |
|  8   |    email     |    電子メール    | varchar  | 254  |      |      |      |      |         |    1     |                                            |
|  9   |   is_staff   |       権限       | tinyint  |  1   |      |      |      |      |         |    1     |                                            |
|  10  |  is_active   |    アクティブ    | tinyint  |  1   |      |      |      |      |         |    1     |                                            |
|  11  | date_joined  |     登録日時     | datetime |      |      |      |      |      |         |    1     |                                            |
|  12  |  nick_name   |     ニック名     | varchar  |  50  |      |      |      |      |         |          |                                            |
|  13  |   birthday   |      誕生日      |   date   |      |      |      |      |      |         |          |                                            |
|  14  |    gender    |       性別       | varchar  |  1   |      |      |      |      |         |    1     |                                            |
|  15  |   address    |     アドレス     | varchar  | 100  |      |      |      |      |         |          |                                            |
|  16  |    mobile    |     電話番号     | varchar  |  11  |      |      |      |      |         |    1     |                                            |
|  17  |    image     |     イメージ     | varchar  | 100  |      |      |      |      |         |    1     |                                            |
|  18  |     name     |      顧客名      | varchar  |  50  |      |      |      |      |         |          |                                            |
|  19  | delivery_flg |    配送フラグ    | tinyint  |  1   |      |      |      |      |         |          | 0:配送元<br/>1:配送先<br/>9:配送元と配送先 |

[^No.1~17はDjangoフレームで作成テーブルのフィールド、No.18~19は追加フィールド]: 

------

#### TTPJM002 配送元マスター

|  No  | カラム名 |    カラムID    |   型    | 桁数 |  PK  | IDX1 | IDX2 | IDX3 | default | not null | 備考 |
| :--: | :------: | :------------: | :-----: | :--: | :--: | :--: | :--: | :--: | :-----: | :------: | :--: |
|  1   |   code   |  配送元コード  | varchar |  10  |      |      |      |      |         |          |      |
|  2   |   name   |    配送元名    | varchar |  50  |      |      |      |      |         |          |      |
|  3   | address  |    アドレス    | varchar | 100  |      |      |      |      |         |          |      |
|  4   |  email   | メールアドレス | varchar |  50  |      |      |      |      |         |          |      |
|  5   |   tel    |      TEL       | varchar |  11  |      |      |      |      |         |          |      |

```
ビューのSQL：
CREATE VIEW TTPJM002 AS 
SELECT
  username AS code
  , name
  , address
  , email
  , mobile AS tel 
FROM
  TTPJM001 
WHERE
  delivery_flg = 0 
  OR delivery_flg = 9
```

------

#### TTPJM003 配送先マスター

|  No  | カラム名 |    カラムID    |   型    | 桁数 |  PK  | IDX1 | IDX2 | IDX3 | default | not null | 備考 |
| :--: | :------: | :------------: | :-----: | :--: | :--: | :--: | :--: | :--: | :-----: | :------: | :--: |
|  1   |   code   |  配送先コード  | varchar |  10  |      |      |      |      |         |          |      |
|  2   |   name   |    配送先名    | varchar |  50  |      |      |      |      |         |          |      |
|  3   | address  |    アドレス    | varchar | 100  |      |      |      |      |         |          |      |
|  4   |  email   | メールアドレス | varchar |  50  |      |      |      |      |         |          |      |
|  5   |   tel    |      TEL       | varchar |  11  |      |      |      |      |         |          |      |

```
ビューのSQL：
CREATE VIEW TTPJM003 AS 
SELECT
  username AS code
  , name
  , address
  , email
  , mobile AS tel 
FROM
  TTPJM001 
WHERE
  delivery_flg = 1 
  OR delivery_flg = 9
```

------

#### TTPJM004 車体マスター

|  No  |   カラム名    |         カラムID         |   型    | 桁数 |  PK  | IDX1 | IDX2 | IDX3 | default | not null | 備考 |
| :--: | :-----------: | :----------------------: | :-----: | :--: | :--: | :--: | :--: | :--: | :-----: | :------: | :--: |
|  1   |    car_id     |          車体ID          | varchar |  5   |      |  1   |      |      |         |    1     |      |
|  2   |   locker_no   |        ロッカーNo        | varchar |  2   |      |  1   |      |      |         |    1     |      |
|  3   |  locker_size  |       ロッカー規格       | tinyint |  1   |      |      |      |      |         |    1     |      |
|  4   | locker_status | ロッカー利用状況(配送ID) | varchar |  15  |      |      |      |      |         |          |      |

------

#### TTPJM005 サービス時間管理マスター

|  No  |      カラム名      |     カラムID     |   型    | 桁数 |  PK  | IDX1 | IDX2 | IDX3 | default | not null | 備考 |
| :--: | :----------------: | :--------------: | :-----: | :--: | :--: | :--: | :--: | :--: | :-----: | :------: | :--: |
|  1   |       car_id       |      車体ID      | varchar |  5   |      |      |      |      |         |    1     |      |
|  2   |        date        |       日付       |  date   |      |      |      |      |      |         |    1     |      |
|  3   | service_start_time | サービス開始時刻 |  time   |      |      |      |      |      |         |          |      |
|  4   |  service_end_time  | サービス終了時刻 |  time   |      |      |      |      |      |         |          |      |
|  5   | return_start_time  | 基地帰還開始時刻 |  time   |      |      |      |      |      |         |          |      |
|  6   |  return_end_time   | 基地帰還終了時刻 |  time   |      |      |      |      |      |         |          |      |

------

#### TTPJM006 汎用コードマスター

|  No  | カラム名 | カラムID |   型    | 桁数 |  PK  | IDX1 | IDX2 | IDX3 | default | not null | 備考 |
| :--: | :------: | :------: | :-----: | :--: | :--: | :--: | :--: | :--: | :-----: | :------: | :--: |
|  1   |   kbn    |   区分   | varchar |  2   |      |  1   |      |      |         |    1     |      |
|  2   |   code   |  コード  | varchar |  10  |      |  1   |      |      |         |    1     |      |
|  3   | content  |   内容   | varchar | 100  |      |      |      |      |         |    1     |      |

------

#### TTPJD001 配送依頼

|  No  |        カラム名         |       カラムID       |    型    | 桁数 |  PK  | IDX1 | IDX2 | IDX3 | default | not null | 備考 |
| :--: | :---------------------: | :------------------: | :------: | :--: | :--: | :--: | :--: | :--: | :-----: | :------: | :--- |
|  1   |      delivery_code      |      配送コード      | varchar  |  10  |      |  1   |      |      |         |    1     |      |
|  2   |       delivery_id       |        配送ID        | varchar  |  15  |      |  1   |      |      |         |    1     |      |
|  3   |    company_code_from    |     配送元コード     | varchar  |  10  |      |      |      |      |         |    1     |      |
|  4   |  company_address_from   |    配送元アドレス    | varchar  | 100  |      |      |      |      |         |          |      |
|  5   |   company_email_from    | 配送元メールアドレス | varchar  |  50  |      |      |      |      |         |          |      |
|  6   |        tel_from         |      配送元TEL       | varchar  |  11  |      |      |      |      |         |          |      |
|  7   |     company_code_to     |     配送先コード     | varchar  |  10  |      |      |      |      |         |    1     |      |
|  8   |   company_address_to    |    配送先アドレス    | varchar  | 100  |      |      |      |      |         |          |      |
|  9   |    company_email_to     | 配送先メールアドレス | varchar  |  50  |      |      |      |      |         |          |      |
|  10  |         tel_to          |      配送先TEL       | varchar  |  11  |      |      |      |      |         |          |      |
|  11  |         car_id          |       配送車ID       | varchar  |  5   |      |      |      |      |         |          |      |
|  12  |        locker_no        |      ロッカーNo      | varchar  |  2   |      |      |      |      |         |          |      |
|  13  | estimated_collect_date  |     予定集荷日時     | datetime |      |      |      |      |      |         |          |      |
|  14  | estimated_delivery_date |     予定受取日時     | datetime |      |      |      |      |      |         |          |      |
|  15  |       status_code       |    配送ステータス    | varchar  |  2   |      |      |      |      |         |          |      |

------

#### TTPJD002 配送状況

|  No  |   カラム名    |   カラムID   |    型    | 桁数 |  PK  | IDX1 | IDX2 | IDX3 | default | not null | 備考 |
| :--: | :-----------: | :----------: | :------: | :--: | :--: | :--: | :--: | :--: | :-----: | :------: | :--- |
|  1   | delivery_code |  配送コード  | varchar  |  10  |      |      |      |      |         |    1     |      |
|  2   |  delivery_id  |    配送ID    | varchar  |  15  |      |      |      |      |         |    1     |      |
|  3   |    car_id     |    車体ID    | varchar  |  5   |      |      |      |      |         |    1     |      |
|  4   |  status_code  |   配送状況   | varchar  |  2   |      |      |      |      |         |    1     |      |
|  5   |   upd_date    | 状態更新日時 | datetime |      |      |      |      |      |         |    1     |      |
|  6   |    remark     |     備考     | varchar  | 200  |      |      |      |      |         |          |      |

------

#### TTPJD003 車体稼働タスク

|  No  |       カラム名       |    カラムID    |    型    | 桁数 |  PK  | IDX1 | IDX2 | IDX3 | default | not null | 備考 |
| :--: | :------------------: | :------------: | :------: | :--: | :--: | :--: | :--: | :--: | :-----: | :------: | :--- |
|  1   |        car_id        |     車体ID     | varchar  |  5   |      |      |      |      |         |    1     |      |
|  2   |     delivery_id      |     配送ID     | varchar  |  15  |      |      |      |      |         |    1     |      |
|  3   |     content_code     |    稼働内容    | varchar  |  2   |      |      |      |      |         |    1     |      |
|  4   | company_address_from | 配送元アドレス | varchar  | 100  |      |      |      |      |         |          |      |
|  5   |  company_address_to  | 配送先アドレス | varchar  | 100  |      |      |      |      |         |          |      |
|  6   |        remark        |      備考      | varchar  | 200  |      |      |      |      |         |          |      |
|  7   |       upd_date       |  状態更新日時  | datetime |      |      |      |      |      |         |    1     |      |