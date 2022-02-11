
## 進め方

* STEP1 学習・理解度UP
  - LINE Blockchainの開発用チャンネル作成・申請
  - LINE Blockchainの チュートリアル読み込み
  - LINE Blockchainの サービストークンとアイテムトークンを学ぶ
  - LINE BITMAX Walletに登録してみる
  - LINE Blockchainでの商品購入を具体例に沿って理解する
  - LINKシネマのサンプルソースコードを読み込む

* STEP2: 
  - LINEブロックチェーンで何を作るか考える

* STEP3
  - 実際にやってみる・作ってみる

## STEP1 学習・理解度UP

### LINE Blockchain開発用チャンネル作成(申請)

- https://developers.line.biz/console/channel/1656844866/blockchain

### チュートリアル読み込み

- https://docs-blockchain.line.biz/ja/service-tutorial/

#### サービストークンとアイテムトークン

- チュートリアルによると、サービストークンは会員向けポイント、アイテムトークンはサービスが具体的に提供する商品・景品などを定義するための概念
    - サービストークンについて
        - サービストークンの定義と概要
            - サービストークンは、LINE Blockchainで取り引きの媒体として使用されます。また、サービス内でサービストークンを景品に交換できるように設計することで、財貨交換の手段として通貨と同じ役割を果たします
            - サービストークンはERC-20と似ているとのこと（互換性はない）
                - ERC-20規格とは - https://www.coindeskjapan.com/99070/
                    - ERC-20規格とは、イーサリアムが定義する規格で、各トークンの核となる機能を標準化したもの
                    - この規格に則って作られたすべてのトークンは互いに互換性があり、またマイイーサウォレット（MyEtherWallet）やメタマスク（MetaMask）などのERC-20対応サービスと互換性がある
                        - ERC-20トークンは通常、プロジェクトの初期段階の資金調達手段として、さまざまな方法で販売される
                            - 過去には、あまりにも過剰な熱狂を呼んだり、怪しげな投資や詐欺の手段となっことで批判された。
                                - 2017年の新規コイン公開（ICO）ブームで資金調達を行ったプロジェクトの多くは、投資家に利益を提供できなかった
                - トークン作成者がゼロからプロジェクトを構築する時に直面するいくつかの問題
                    - スマートコントラクトの作成
                        - トークンの全供給量やトークンの流通方法、発行スケジュールなどを決める事が必要
                        - スマートコントラクトは、トークンの全供給量やトークンの流通方法、発行スケジュールなどを決める際に、きわめて重要な役割を担う。
                            - 保有者の残高を確認したり、トークンの移動を円滑にするなどの主要な機能も担う。
                        - こうしたスマートコントラクトの記述は、複雑で時間のかかるプロセス
                            - 通常は専門の開発者チームが必要
                            - 非常にコストがかかること
                            - スマートコントラクトが正しくプログラミングされていなければ、壊滅的な影響を及ぼす可能性がある。
                    - ウォレットや取引所との互換性
                        - ERC-20規格を使わずに暗号資産を作成すると、ウォレットや取引所などとの互換性を確保するために追加作業が必要
        - サービストークンの具体例と使い方
            - サービストークンで会員ポイントの仕組みを設計する
                - MovieToken(MOV)という名前のサービストークンを定義 https://docs-blockchain.line.biz/ja/service-tutorial/Step1#step1-3
                - 映画鑑賞券を購入時に(LINE Blockchainのbase coinsで映画鑑賞券を購入したユーザに)、200 MovieToken(MOV)が与えられる https://docs-blockchain.line.biz/ja/service-tutorial/Step6
                    - 購入額の一部をポイント還元され、溜まったポイントは映画鑑賞券に交換できる 
                - MovieToken(MOV)で、映画鑑賞券を購入可能。くわしくはサンプルコードを参照 https://github.com/line/blockchain-sample-link-cinema/blob/master/controller/ticket.go
                    - LINE Blockchainのbase coinsでも映画鑑賞券を購入できるし、MovieToken(MOV)を一定量持っている場合MovieToken(MOV)を使って映画鑑賞券を購入することもできる
    - アイテムトークンについて 
        - アイテムトークンの定義と概要
            - アイテムトークンとは、サービスで使用する財貨やアイテムのこと
            - サービストークンとは違ってすべて同じContract IDを持ち
            - Token IDで区別します
            - アイテムトークンは、fungiblesとnon-fungiblesに分けることができます。性質に応じて適切なタイプを選択する必要があります
            - Fungibleアイテムトークン
                - 同じToken IDでトークンの価値や性格も同じ
            - Non-fungibleアイテムトークン
                - それぞれのトークンが固有のToken IDを持っているため、トークンの価値や性格も異なります  
        - アイテムトークンの具体例と使い方
            - 映画鑑賞券として使うアイテムトークンを定義することを考える https://docs-blockchain.line.biz/ja/service-tutorial/Step2
                - 映画鑑賞券に付随する情報と特徴
                    - 映画鑑賞券に付随する情報
                    - 上映館
                    - 上映日
                    - 座席
                    - 特徴
                    - 他の観客が、同じ映画館、同じ日付、同じ座席を選択できない
                        - Aという映画の鑑賞券は上映館、上映日、座席が固有なものである
                - 映画鑑賞券は、「Fungibleアイテムトークン」 と 「Non-fungibleアイテムトークン」どちらのアイテムトークンとして設計すべきか?
                    - 答え: Non-fungibleアイテムトークン
                    - 理由: 固有の情報が入っているnon-fungibleが適切


#### LINE Blockchainで商品購入機能を実装する方法(仕組み)を理解する
- ウォレット内のコイン(TestCoin)で、映画鑑賞券を購入することを考える
  - 映画鑑賞券を購入するということは
    - ユーザーウォレットにあるTest Coin と サービスウォレットにあるMovieTicketアイテムトークンを交換すること
      - サービスウォレットは、サービス作成時に作られる在庫管理用の入れ物
      - MovieTicketアイテムトークンは、映画鑑賞券に付随する固有の情報を含むNFTトークン

### LINE BITMAX Walletに登録してみる
- ユーザーは、LINE BITMAX Walletに登録する必要がある
  - LINE Blockchainのサービス登録とは別に、LINE BITMAX Walletに登録する必要がある
    - サービスへの登録手続きにLINE BITMAX Walletへの登録を含めることもできます。
  - LINE BITMAX Walletに登録した後
    - ユーザーは自分のLINE IDに1対1で紐付けられるウォレットを取得
    - 保有するトークンの取得や転送ができるようになります
  -  ユーザーウォレットからサービスにトークンを転送する方法
    - https://docs-blockchain.line.biz/ja/service-tutorial/Step5
      - ユーザーはLINE BITMAX WalletにあるTest Coin (TC)でLINKシネマの映画鑑賞券を購入
        - Test Coinで映画鑑賞券を購入するということは
          - ユーザーウォレットにあるTest Coin
          - と
          - サービスのサービスウォレットにあるMovieTicketアイテムトークン
      - 購入額の一部を会員ポイントとして与える
        - サービストークンのMovieToken (MOV)を会員ポイントとして使用
          - 映画鑑賞券を購入した観客のウォレットに、200 MOVを転送
            - https://docs-blockchain.line.biz/ja/api-guide/category-service-wallets/transfer#v1-wallets-walletAddress-service-tokens-contractId-transfer-post

### LINKシネマのサンプルソースコードを読み込む　https://docs-blockchain.line.biz/ja/sample-services/Link-cinema

- 0. 準備

    - ソース取得 
        - git clone https://github.com/line/blockchain-sample-link-cinema

        - LINKシネマのサーバー
            - 実行と同時にconfiguration.tomlに入力したUser IDでログイン

        - 映画鑑賞券を買うには
            - ログインしたアカウントがTest Coin（TC、base coin）や会員ポイント(MovieToken、サービス トークン)、割引クーポン(MovieDiscount、アイテムトークン)を保有する必要があります
            - サービスウォレットに十分な資産を持っている必要があります。

- 1. トークン転送

  - 以下のAPIを呼び出して、当該アカウントに100 TCと10,000の会員ポイント、割引クーポン10枚を送ります。
    - curl -X GET 'localhost:8080/api/v0/test/init' -H 'accept: application/json'
      - 作業が成功すると、Test Coin、会員ポイント、割引クーポンを鋳造または転送した3つのトランザクションのtxHashが配列で表示されます。
            [
                "7E86A7BD290E82DEB16CCB2047FD3FC9DC939383E6E1D4BCAE22FD188DADDB7A",
                "9BB1BAC5144D8BD98D05A6BB05AE89F743ECB09F7E02BC4952AD30F6DCA288EC",
                "9C251F696B1CFA1611A292E518C06EA1034E38C33B9B97CC7336B598E6A71653"
            ]

- 2. トランザクションを確認する#
  - 1.で受信したtxHashでトランザクションの状態を取得するAPIを呼び出してください。
      - curl -X GET 'localhost:8080/api/v0/test/transaction?txhash=9C251F696B1CFA1611A292E518C06EA1034E38C33B9B97CC7336B598E6A71653' -H 'accept: application/json'
  - 以下のように詳細なフィールド値が表示され、トランザクションの状態を見て前の作業が完了したかを確認できます。（トランザクションが確定されるまではフィールド値が表示されません。）

```
{
  "height": 1580820,
  "txhash": "9C251F696B1CFA1611A292E518C06EA1034E38C33B9B97CC7336B598E6A71653",
  "index": 0,
  "code": 0,
  "raw_log": "",
  "logs": [
    {
      "msg_index": 0,
      "success": true,
      "log": "",
      "events": [
        {
          "type": "message",
          "attributes": [
            {
              "key": "module",
              "value": "collection"
            },
            {
              "key": "sender",
              "value": "tlink1d2rthnzttepecqttzwxrev29ny06gfq6ead9n6"
            },
            {
              "key": "action",
              "value": "mint_ft"
            }
          ]
        },
        {
          "type": "mint_ft",
          "attributes": [
            {
              "key": "contract_id",
              "value": "d339958f"
            },
            {
              "key": "from",
              "value": "tlink1d2rthnzttepecqttzwxrev29ny06gfq6ead9n6"
            },
            {
              "key": "to",
              "value": "tlink1jtsgy50xxw72pugn3u8rs5palj5czt59f8mmys"
            },
            {
              "key": "amount",
              "value": "10:0000000100000000"
            }
          ]
        }
      ]
    }
  ],
  "gasWanted": 100000000,
  "gasUsed": 34599,
  "tx": {...},
  "timestamp": 1606885179000
}
```

3. プロキシを設定する

- プロキシ設定とは
  - LINE BITMAX Walletのユーザーウォレットにあるアイテムトークン管理権限をサービスに委任すること
    - LINE BITMAX Walletを円滑に利用するには、ユーザーウォレットにあるアイテムトークンを管理できる権限をサービスに委任する必要があります。

- プロキシ設定は、自動化できるのか?
  - ユーザの認証操作のcallbackをwebhookで受信できれば可能..?
    - https://docs.blockchain.line.me/ja/api-guide/Callback-Response
      - トランザクションが発生するAPIリクエストは、トランザクションがブロックに記録されたとき、raw transactionをcallback応答として受け取ることができます。
        - アイテムトークンに関するメッセージタイプ
          - collection/MsgApprove#
          - アイテムトークンを管理する権限の委任をリクエストするメッセージです。

- プロキシ設定3STEP
  - プロキシは、以下の３段階をすべて完了すると設定されます。
        - ① プロキシ設定APIを呼び出し、LINE BITMAX Walletにリクエスト（サービス側で実行）
          - curl -X GET 'localhost:8080/api/v0/user/proxy' -H 'accept: application/json'
        - ユーザーの承認のためのリクエストセッショントークンとリダイレクトURIが表示されます。

```
{
  "requestSessionToken": "ZRq8W5oht6cs-MOK**********",
  "redirectUri": "https://lbw.line.me/grant/proxy/ZRq8W5oht6cs***********"
}
```

        - ② 1のレスポンスとして受け取ったリダイレクトURIにより、LINE BITMAX Walletに移動した後、プロキシ設定を受け入れて認証（ユーザーが実行）
          - https://lbw.line.me/grant/proxy/ZRq8W5oht6cs***********
        - ③ プロキシコミット（commit）APIを呼び出し、トランザクションをコミットし、txHashを受け取って確認の受け取りおよび確認(サービス側で実行）
          - 承認が終わると、ステップ①で取得した"requestSessionToken"をpathパラメータで入力し、以下のAPIを呼び出してプロキシ設定をコミットします
          - curl -X GET 'localhost:8080/api/v0/user/proxy/commit/ZRq8W5oht6cs-MOK**********' -H 'accept: application/json'
          - レスポンスとしてプロキシ設定トランザクションのtxHashを受け取ります。
            - 199EB7BFD99EACF4B5D57DFC0E0696E5039F91A3383125E2BF27600531648DC3
              - レスポンスとしてプロキシ設定トランザクションのtxHashを受け取ったあと、そのハッシュ文字列を用いてなんの処理を実行する必要がありますか？もしくは何もする必要がない場合、通常このハッシュ値は受け取ったあとどのように保管・管理されますか？

```
{
  "codespace": "token",
  "code": 24,
      "index": int,
  "height": int,
  "txhash": string,
  "data": string,
  "logs": [
    {
      "msgIndex": int,
      "log": string,
      "events": [
        {
          "type": string,
          "attributes": [
            {
              "key": string,
              "value": string
            }
            ...
        },
        ...
      ]
    }
    ...
  ],
  "info": string,
  "gasWanted": string,
  "gasUsed": string,
  "tx": {
    "type": "cosmos-sdk/StdTx",
    "value": {
      "msg": [
        {
          "type": "collection/MsgApprove",
          "value": {
              "approver":	"<権限を委任するウォレットアドレス>",
              "contractId":	"<権限を委任するアイテムトークンcollectionのcontract ID>",
              "proxy":	"<権限を委任されるウォレットアドレス>"
          }
        }
        ...
      ],
      "fee": {
        "amount": [],
        "gas": string
      },
      "signatures": [
        {
          "pubKey": {
            "type": string,
            "value": string
          },
          "signature": string
        }
      ],
      "memo": string
    }
  },
  "timestamp": long
}
```



4. 映画鑑賞券を購入する#

- 販売中の映画鑑賞券をLINE BITMAX Walletで決済します。
  - Test Coin（TC）と会員ポイント（MOV、サービス トークン）、割引クーポン（アイテムトークン）を全部使用します。 
    - まず、Test Coinと会員ポイントをサービスウォレットに転送します。
    - 規格が異なるトークンを同時に送信する機能がない
      - 規格ごとに分けて処理します。
        - １つは14TCを送る作業
        - もう１つは1,000の会員ポイントを送る作業

- Test Coinの決済APIを呼び出し
  - このリクエストは、ユーザーウォレットからサービスウォレットに14TCを送信するようにリクエストします。

```
curl -X POST 'localhost:8080/api/v0/ticket/purchase' -H 'accept: application/json' \
-d '{
  "movieInfo": {
      "title": "The LINK Movie",
      "score": 4.9,
      "country": "South Korea",
      "runningTime": 132,
      "genre": "Drama",
      "year": 2020
    },
    "ticketInfo": {
      "date": "2020-02-01T03:30:00+09:00",
      "theater": "Seoul, World Tower, Theater 1",
      "amount": 1,
      "sit": "M14",
      "price": 20
    },
    "priceInfo": {
      "usedFungible": 1,
      "usedServiceToken": 1000,
      "subTotal": 20,
      "discount": -6,
      "grandTotal": 14
    }
  }'
```

  - ユーザーに承認をリクエストするための情報が出力されます。

```
{
  "requestSessionToken": "wlPHSLhwD6CQV2h************",
  "redirectUri": "https://lbw.line.me/grant/transfer/wlPHSLhwD6CQV2hE8**********"
}
```

- "requestSessionToken"をメモし、"redirectUri"に移動して決済を承認します。 (TODO: 実際は画面を対象URLにリダイレクトして、ユーザに承認を求める必要がある)

- 次に、会員ポイントを転送します。上記の映画鑑賞券の情報を利用して以下のAPIを呼び出します。
  - このリクエストは、ユーザーウォレットからサービスウォレットに1,000MOVを送信します。

```
curl -X POST 'localhost:8080/api/v0/ticket/purchase/extra' -H 'accept: application/json'
-d '{
    "movieInfo": {
      "title": "The LINK Movie",
      "score": 4.9,
      "country": "South Korea",
      "runningTime": 132,
      "genre": "Drama",
      "year": 2020
    },
    "ticketInfo": {
      "date": "2020-02-01T03:30:00+09:00",
      "theater": "Seoul, World Tower, Theater 1",
      "amount": 1,
      "sit": "M14",
      "price": 20
    },
    "priceInfo": {
      "usedFungible": 1,
      "usedServiceToken": 1000,
      "subTotal": 20,
      "discount": -6,
      "grandTotal": 14
    }
}'
```


- ユーザーの承認をリクエストするための情報が出力されます

```
{
    "requestSessionToken": "C2hYYPf3amjtHlXiZ**********",
    "redirectUri": "https://lbw.line.me/grant/transfer/C2hYYPf3amjtHlXi**********"
}
```

- "requestSessionToken"をメモし、"redirectUri"に移動して決済を承認します。(TODO: 実際は画面を対象URLにリダイレクトして、ユーザに承認を求める必要がある)
  - ユーザーの承認後にもトランザクションをコミットするまでは、資産の転送が行われません。


5. 購入確定および鑑賞券を転送する#

- 決済トランザクションをコミットし、購入を確定して資産を転送します
  - 4.の決済でユーザの承認が得られた場合でも、トランザクションをコミットしないと、決済が行われません。
    - 決済トランザクションをコミットし、購入を確定して初めて資産が転送される仕組みです(TODO: コミットをどこで行うか設計が必要)
  - 以下のように先にメモした2つの"requestSessionToken"をpathパラメータとして入力し、APIを呼び出してください。
    - 4つのトランザクションを作成します。
      - Test Coinの決済トランザクション
        - 映画鑑賞券を購入するで承認したとおりユーザーウォレットからサービスウォレットに14TCを転送します。
      - 会員ポイントの決済およびリワードトランザクション
        - 映画鑑賞券を購入するで承認したとおりユーザーウォレットからサービスウォレットに1,000 MOVを転送します。
      - 映画鑑賞券の鋳造トランザクション
        - ユーザーが購入した映画鑑賞券をnon-fungibleアイテムトークンで鋳造し、ユーザーウォレットに転送します。
      - 割引クーポンの焼却トランザクション
        - 映画鑑賞券を購入するで使用した割引クーポン1枚をユーザーウォレットで焼却します。

```
curl -X POST 'localhost:8080/api/v0/ticket/purchase/commit/wlPHSLhwD6CQV2h************/C2hYYPf3amjtHlXiZ**********' -H 'accept: application/json' \
-d '{
    "movieInfo": {
      "title": "The LINK Movie",
      "score": 4.9,
      "country": "South Korea",
      "runningTime": 132,
      "genre": "Drama",
      "year": 2020
    },
    "ticketInfo": {
      "date": "2020-02-01T03:30:00+09:00",
      "theater": "Seoul, World Tower, Theater 1",
      "amount": 1,
      "sit": "M14",
      "price": 20
    },
    "priceInfo": {
      "usedFungible": 1,
      "usedServiceToken": 1000,
      "subTotal": 20,
      "discount": -6,
      "grandTotal": 14
    }
}'
```

### 処理シーケンスを具体的に記述する

- ユーザ招待(テスト用コインの付与)

![img](http://www.plantuml.com/plantuml/proxy?fmt=svg&src=https://raw.githubusercontent.com/Eigo-Mt-Fuji/portfolio-2022/main/docs/line-blockchain-initial-transfer.txt)

- ログインフロー

![img](http://www.plantuml.com/plantuml/proxy?fmt=svg&src=https://raw.githubusercontent.com/Eigo-Mt-Fuji/portfolio-2022/main/docs/line-blockchain-login-with-proxy.txt?hoge=true)

### LINE Blockchain APIをSDK経由で実行してみる?

```
 curl -v -X POST https://test-api.blockchain.line.me/v1/item-tokens/59de2003/non-fungibles/10000001/mint -H "Content-Type: application/json" -H "service-api-key: 416b9d42-d2ce-431b-800b-6757e1adf83d" -H "nonce: d23bd1ba" -H "timestamp: 1643629852531" -H 'signature: PHclZF60qHbXJxIdV/Ijesm7kftyNg4D8K8KmAU8L38EdKB2IBEsCh0Qxqms2XlQZTSdu2XYTg3UMxWcmBjZpw==' -d '{"ownerAddress":"tlink1aavw9sk4349t3swa49l3zjmzd5cl4v46uxjc4m","ownerSecret":"psip40921cEiz64+e8hJWV2L+4j1GreQ/URnpV+2ocY=","name":"EI5NFT","toAddress":"tlink1g99r4sersjjn8p6jjjp566lt2tr0pr53wh9erg"}'
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 147.92.139.88...
* TCP_NODELAY set
* Connected to test-api.blockchain.line.me (147.92.139.88) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/cert.pem
  CApath: none
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server accepted to use h2
* Server certificate:
*  subject: C=JP; ST=Tokyo-to; L=Shinjuku-ku; O=LINE Corporation; CN=*.blockchain.line.me
*  start date: May 10 07:21:03 2021 GMT
*  expire date: Jun 11 07:21:03 2022 GMT
*  subjectAltName: host "test-api.blockchain.line.me" matched cert's "*.blockchain.line.me"
*  issuer: C=BE; O=GlobalSign nv-sa; CN=GlobalSign RSA OV SSL CA 2018
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7f9cf8809600)
> POST /v1/item-tokens/59de2003/non-fungibles/10000001/mint HTTP/2
> Host: test-api.blockchain.line.me
> User-Agent: curl/7.64.1
> Accept: */*
> Content-Type: application/json
> service-api-key: 416b9d42-d2ce-431b-800b-6757e1adf83d
> nonce: d23bd1ba
> timestamp: 1643629852531
> signature: PHclZF60qHbXJxIdV/Ijesm7kftyNg4D8K8KmAU8L38EdKB2IBEsCh0Qxqms2XlQZTSdu2XYTg3UMxWcmBjZpw==
> Content-Length: 199
> 
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
* We are completely uploaded and fine
< HTTP/2 202 
< date: Mon, 31 Jan 2022 11:50:56 GMT
< content-type: application/json
< content-length: 168
< x-ratelimit-remaining: 19
< x-ratelimit-replenish-rate: 20
< x-envoy-upstream-service-time: 151
< x-envoy-decorator-operation: prod-api-gateway.link-developers.svc.cluster.local:28083/*
< strict-transport-security: max-age=15724800; includeSubDomains
< 
* Connection #0 to host test-api.blockchain.line.me left intact
{"responseTime":1643629856952,"statusCode":1002,"statusMessage":"Accepted","responseData":{"txHash":"5E3940C3A93C917DFBF238C41A7A9853524EC76CA28178593622254D7E05A734"}}* Closing connection 0
```

## STEP2: LINEブロックチェーンで何を作るか考える

- 先着配布、メンバーシップ、ストックオプション型で何かを作ればいい気がした。
  - 限られた資金で、多くの人を集める
    - 先着配布: 急いで参加させる
    - 抽選（CP終了後）: とりあえずみんなに参加させる
    - 抽選（即時、当選上限あり）: とりあえずみんなに参加させつつ、急いで応募させる
  - ロイヤリティの高いユーザを集める
    - メンバーシップ・会員特典
    - 招待（インビテーション）方式
    - ストックオプション
      - 何に交換できるのか、どのくらいの価値が出るのか決まっていない証券・トークンを配布する
      - 即時性のない特典要素。おしゃれやコレクション的な意味。
      - ブランドやプロダクトに期待があれば、ユーザの集客効果が期待できる

## STEP3: 実際にやってみる・作ってみる

https://github.com/Eigo-Mt-Fuji/eigo-nft

