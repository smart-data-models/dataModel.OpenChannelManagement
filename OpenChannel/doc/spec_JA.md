<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティオープンチャンネル  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/OpenChannel/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**このエンティティは、原水(オープンチャンネル)システム管理領域のために作られた一般的なチャンネルの調和された記述を含む。  
バージョン: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bottomSlope[number]`: 水路の底勾配。単位はすべてCEFACTコード  - `bottomWidth[number]`: 水路の底幅（「台形」形状の場合）。単位はすべてCEFACTコード  - `celerity[number]`: 水門の開閉後に水路に沿って伝播するサージの速度  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `diameter[number]`: 円形チャネルの直径。単位はすべてCEFACTコード  - `downstreamNode[*]`: チャネルが終了する下流ノード（例：ジャンクション、レギュレーション構造）のIDを示す関係。  - `flowType[string]`: 水路の流れのタイプを定義するテキスト。Enum:'Free-Surface flow' (自由表面流)  - `geometryType[string]`: 水路の形状。Enum:'台形, 円形'].  - `id[*]`: エンティティの一意識別子  - `leftSideSlope[number]`: 水路の左岸の勾配（「台形」形状の場合）。単位はすべてCEFACTコード  - `length[number]`: チャンネルの長さ。単位はすべてCEFACTコード  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `maxWaterDepth[number]`: 水路の最大許容水深。単位はすべてCEFACTコード  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `rightSideSlope[number]`: 水路の右岸の勾配（「台形」形状の場合）。単位はすべてCEFACTコード  - `roughnessCoefficient[number]`: マニングの粗さ係数  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `tag[string]`: オプションのテキスト文字列。  . Model: [https://schema.org/Text](https://schema.org/Text)- `travelDuration[number]`: 下流ノード（すなわちレギュレーション・ストラクチャー）から上流ノードに伝わるサージの継続時間  - `type[string]`: NGSI-LDエンティティ・タイプ。OpenChannelでなければならない。  - `upstreamNode[*]`: チャンネルが始まる上流ノード（例：ジャンクション、レギュレーション構造）のIDを示す関係。  - `waterLoss[number]`: 水路からの漏水/損失 - 水路の流量に対する割合または数値（流量）  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OpenChannel:    
  description: This entity contains a harmonised description of a generic Channel made for Raw-Water (Open Channels) System Management domain.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    downstreamNode:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: 'A relationship indicating the ID of the downstream node (e.g., Junction, Regulation Structure), where the channel ends'    
      x-ngsi:    
        type: Relationship    
    geometry:    
      description: Description of the geometry of the channel    
      properties:    
        bottomSlope:    
          description: The bottom slope of the channel. All units are accepted in CEFACT code    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        bottomWidth:    
          description: The bottom width of the channel (for 'Trapezoidal' geometry). All units are accepted in CEFACT code    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        celerity:    
          description: Velocity of a surge propagated along the channel after the opening or close of a sluice gate    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        diameter:    
          description: The diameter of a circular channel. All units are accepted in CEFACT code    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        flowType:    
          description: 'Text defining the type of flow in the channel. Enum:''Free-Surface flow'''    
          enum:    
            - Free-Surface flow    
          type: string    
          x-ngsi:    
            type: Property    
        geometryType:    
          description: 'The geometry of the channel. Enum:''Trapezoidal, Circular'']'    
          enum:    
            - Circular    
            - Trapezoidal    
          type: string    
          x-ngsi:    
            type: Property    
        leftSideSlope:    
          description: The slope of the left bank of the channel (for 'Trapezoidal' geometry). All units are accepted in CEFACT code    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        length:    
          description: The length of the channel. All units are accepted in CEFACT code    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        maxWaterDepth:    
          description: The maximum allowable water depth in the channel. All units are accepted in CEFACT code    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        rightSideSlope:    
          description: The slope of the right bank of the channel (for 'Trapezoidal' geometry). All units are accepted in CEFACT code    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        roughnessCoefficient:    
          description: The Manning’s roughness coefficient    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        travelDuration:    
          description: 'The duration of the surge travelling from the downstream node (i.e., Regulation Structure) to the upstream node'    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        waterLoss:    
          description: Water leakages/losses from the channel - percentage of flow of the channel or a number (flow)    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    tag:    
      description: An optional text string used to qualify an item    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI-LD Entity Type. it has to be OpenChannel    
      enum:    
        - OpenChannel    
      type: string    
      x-ngsi:    
        type: Property    
    upstreamNode:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: 'A relationship indicating the ID of the upstream node (e.g., Junction, Regulation Structure), where the channel begins'    
      x-ngsi:    
        type: Relationship    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/OpenChannel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/Channel/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### OpenChannel NGSI-v2 キー値の例  
JSON-LD形式のOpenChannelのkey-valuesの例です。これは NGSI-v2 と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Channel:id:IXPY:98787462",  
  "type": "OpenChannel",  
  "dateCreated": "2021-04-13T21:22:33Z",  
  "dateModified": "2021-04-13T23:34:18Z",  
  "source": "",  
  "name": "Section 3",  
  "alternateName": "S-3",  
  "description": "Description of the channel S-3",  
  "dataProvider": "",  
  "owner": [  
    "urn:ngsi-ld:Channel:items:ZOOU:49614637",  
    "urn:ngsi-ld:Channel:items:ODUZ:33451005"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Channel:items:YJSD:41528487",  
    "urn:ngsi-ld:Channel:items:MROT:86526209"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -14.2004135,  
      -147.354695  
    ]  
  },  
  "address": {  
    "streetAddress": "",  
    "addressLocality": "Thesalonikii",  
    "addressRegion": "",  
    "addressCountry": "HELLAS",  
    "postalCode": "",  
    "postOfficeBoxNumber": "",  
    "areaServed": "."  
  },  
  "areaServed": "",  
  "downstreamNode": "urn:ngsi-ld:Channel:downstreamNode:DQUS:63966588",  
  "upstreamNode": "urn:ngsi-ld:Channel:upstreamNode:MBQH:53312123",  
  "tag": "Something special enjoy research institution past western. System spring clearly impact policy.",  
  "geometry": {  
    "geometryType": "Trapezoidal",  
    "bottomSlope": 12,  
    "leftSideSlope": 14,  
    "rightSideSlope": 3,  
    "bottomWidth": 5,  
    "diameter": 0,  
    "maxWaterDepth": 4,  
    "roughnessCoefficient": 0.6,  
    "flowType": "Free-Surface flow",  
    "celerity": 5,  
    "travelDuration": 22,  
    "waterLoss": 0.12,  
    "length": 15  
  }  
}  
```  
</details>  
#### OpenChannel NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の OpenChannel の例です。これは、オプションを使用しない場合は NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "IXPY.98787462",  
  "type": "OpenChannel",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2021-04-13T21:22:33Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2021-04-13T23:34:18Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Section 3"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "S-3"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Description of the channel S-3"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": ""  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Channel:items:ZOOU:49614637",  
      "urn:ngsi-ld:Channel:items:ODUZ:33451005"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Channel:items:YJSD:41528487",  
      "urn:ngsi-ld:Channel:items:MROT:86526209"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -14.2004135,  
        -147.354695  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "",  
      "addressLocality": "Thesalonikii",  
      "addressRegion": "",  
      "addressCountry": "HELLAS",  
      "postalCode": "",  
      "postOfficeBoxNumber": "",  
      "areaServed": "."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": ""  
  },  
  "downstreamNode": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Channel:downstreamNode:DQUS:63966588"  
  },  
  "upstreamNode": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Channel:upstreamNode:MBQH:53312123"  
  },  
  "tag": {  
    "type": "Text",  
    "value": "Something special enjoy research institution past western. System spring clearly impact policy."  
  },  
  "geometry": {  
    "type": "StructuredValue",  
    "value": {  
      "geometryType": "Trapezoidal",  
      "bottomSlope": 12,  
      "leftSideSlope": 14,  
      "rightSideSlope": 3,  
      "bottomWidth": 5,  
      "diameter": 0,  
      "maxWaterDepth": 4,  
      "roughnessCoefficient": 0.6,  
      "flowType": "Free-Surface flow",  
      "celerity": 5,  
      "travelDuration": 22,  
      "waterLoss": 0.12,  
      "length": 15  
    }  
  }  
}  
```  
</details>  
#### OpenChannel NGSI-LD キー値の例  
JSON-LD形式のOpenChannelのkey-valuesの例です。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Channel:id:IXPY:98787462",  
  "type": "OpenChannel",  
  "address": {  
    "streetAddress": "",  
    "addressLocality": "Thesalonikii",  
    "addressRegion": "",  
    "addressCountry": "HELLAS",  
    "postalCode": "",  
    "postOfficeBoxNumber": "",  
    "areaServed": "."  
  },  
  "alternateName": "S-3",  
  "areaServed": "",  
  "dataProvider": "",  
  "dateCreated": "2021-04-13T21:22:33Z",  
  "dateModified": "2021-04-13T23:34:18Z",  
  "description": "Description of the channel S-3",  
  "downstreamNode": "urn:ngsi-ld:Channel:downstreamNode:DQUS:63966588",  
  "geometry": {  
    "geometryType": "Trapezoidal",  
    "bottomSlope": 12,  
    "leftSideSlope": 14,  
    "rightSideSlope": 3,  
    "bottomWidth": 5,  
    "diameter": 0,  
    "maxWaterDepth": 4,  
    "roughnessCoefficient": 0.6,  
    "flowType": "Free-Surface flow",  
    "celerity": 5,  
    "travelDuration": 22,  
    "waterLoss": 0.12,  
    "length": 15  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -14.2004135,  
      -147.354695  
    ]  
  },  
  "name": "Section 3",  
  "owner": [  
    "urn:ngsi-ld:Channel:items:ZOOU:49614637",  
    "urn:ngsi-ld:Channel:items:ODUZ:33451005"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Channel:items:YJSD:41528487",  
    "urn:ngsi-ld:Channel:items:MROT:86526209"  
  ],  
  "source": "",  
  "tag": "Something special enjoy research institution past western. System spring clearly impact policy.",  
  "upstreamNode": "urn:ngsi-ld:Channel:upstreamNode:MBQH:53312123",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### OpenChannel NGSI-LD 正規化例  
以下は、正規化された JSON-LD フォーマットの OpenChannel の例です。これは、オプションを使わない場合の NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Channel:id:IXPY:98787462",  
  "type": "OpenChannel",  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "",  
      "addressLocality": "Thesalonikii",  
      "addressRegion": "",  
      "addressCountry": "HELLAS",  
      "postalCode": "",  
      "postOfficeBoxNumber": "",  
      "areaServed": "."  
    }  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "S-3"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": ""  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": ""  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-04-13T21:22:33Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-04-13T23:34:18Z"  
    }  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description of the channel S-3"  
  },  
  "downstreamNode": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Channel:downstreamNode:DQUS:63966588"  
  },  
  "geometry": {  
    "type": "Property",  
    "value": {  
      "geometryType": "Trapezoidal",  
      "bottomSlope": 12,  
      "leftSideSlope": 14,  
      "rightSideSlope": 3,  
      "bottomWidth": 5,  
      "diameter": 0,  
      "maxWaterDepth": 4,  
      "roughnessCoefficient": 0.6,  
      "flowType": "Free-Surface flow",  
      "celerity": 5,  
      "travelDuration": 22,  
      "waterLoss": 0.12,  
      "length": 15  
    }  
  },  
  "location": {  
    "type": "Georoperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -14.2004135,  
        -147.354695  
      ]  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "Section 3"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Channel:items:ZOOU:49614637",  
      "urn:ngsi-ld:Channel:items:ODUZ:33451005"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Channel:items:YJSD:41528487",  
      "urn:ngsi-ld:Channel:items:MROT:86526209"  
    ]  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "tag": {  
    "type": "Property",  
    "value": "Something special enjoy research institution past western. System spring clearly impact policy."  
  },  
  "upstreamNode": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Channel:upstreamNode:MBQH:53312123"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
