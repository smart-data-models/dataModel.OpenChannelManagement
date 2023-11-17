<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティクロスセクション    
==============<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/CrossSection/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな記述：**このエンティティには、原水(開水路)システム管理領域用に作成された一般的な Cross-Section の調和された記述が含まれる。CrossSection は、原水の特性が装置によって監視され、シミュレーションによって計算されるシステムの任意のポイントを定義する。    
バージョン: 0.0.1    
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `attachedTo[*]`: 断面が「住んでいる」チャネルのIDとの関係。Channel型のエンティティへの参照。  - `bottomSlope[number]`: 断面が「住む」水路の底勾配。単位はすべてCEFACTコード  - `bottomWidth[number]`: 断面の底幅（「台形」形状の場合）。単位はすべてCEFACTコード  - `crossSectionGeometry[string]`: 断面の形状。Enum:'円形、台形'  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `diameter[number]`: 円形断面の直径  - `energyHead[number]`: 断面における全エネルギーヘッド  - `id[*]`: エンティティの一意識別子  - `inheritsFrom[*]`: プロパティの値が取得されるチャンネルコンポーネントのURI  - `leftSideSlope[number]`: 断面の左岸の勾配（「台形」形状の場合）。単位はすべてCEFACTコード  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `maxWaterDepth[number]`: 断面における最大許容水深。単位はすべてCEFACTコード  - `name[string]`: このアイテムの名前  - `observedBy[*]`: 原水の特性を監視する装置のIDとの関係  . Model: [https://smart-data-models.github.io/dataModel.Device/device-schema.json](https://smart-data-models.github.io/dataModel.Device/device-schema.json)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `position[object]`: 他の要素との距離や、それらの要素との関係に関する情報を提供するオブジェクト。  	- `distance[number]`: このエンティティと基準点（例えば、システムの最上流点）との間の距離。      
- `rightSideSlope[number]`: 断面の右岸の勾配（「台形」形状の場合）。単位はすべてCEFACTコード  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `specificConductivity[number]`: 断面における水の伝導率  - `tag[string]`: オプションのテキスト文字列。  . Model: [https://schema.org/Text](https://schema.org/Text)- `turbidity[number]`: 断面における水の濁度  - `type[string]`: NGSI-LD エンティティタイプ。CrossSectionでなければならない。  - `waterFlow[number]`: 断面での水の流れ  - `waterLevel[number]`: 断面の水位  - `waterTemperature[number]`: 断面の水温  - `waterVelocity[number]`: 断面の水流  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
CrossSection:      
  description: This entity contains a harmonised description of a generic Cross-Section made for Raw-Water (Open Channels) System Management domain. A CrossSection defines any point of the system where raw-water properties are monitored by a device and/or computed via simulation.      
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
    attachedTo:      
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
      description: A relationship to the ID of the channel where the cross-section 'lives in'. Reference to an entity of type Channel      
      x-ngsi:      
        type: Relationship      
    bottomSlope:      
      description: The bottom slope of the channel where the cross-section 'lives in'. All units are accepted in CEFACT code      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    bottomWidth:      
      description: The bottom width of the cross-section (for 'Trapezoidal' geometry). All units are accepted in CEFACT code      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    crossSectionGeometry:      
      description: 'The geometry of the cross-section. Enum:''Circular, Trapezoidal'''      
      enum:      
        - Circular      
        - Trapezoidal      
      type: string      
      x-ngsi:      
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
    diameter:      
      description: The diameter of a circular cross-section      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    energyHead:      
      description: The total energy head at the cross-section      
      type: number      
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
    inheritsFrom:      
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
      description: URI of a Channel component from which the value of a property is obtained      
      x-ngsi:      
        type: Relationship      
    leftSideSlope:      
      description: The slope of the left bank of the cross-section (for 'Trapezoidal' geometry). All units are accepted in CEFACT code      
      minimum: 0      
      type: number      
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
    maxWaterDepth:      
      description: The maximum allowable water depth at the cross-section. All units are accepted in CEFACT code      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    observedBy:      
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
      description: A relationship to the ID of the device that monitors raw-water properties      
      x-ngsi:      
        model: https://smart-data-models.github.io/dataModel.Device/device-schema.json      
        type: Relationship      
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
    position:      
      description: Object providing information about the distance with the rest of the elements and a relationship with them      
      properties:      
        distance:      
          description: 'The distance between this Entity and a reference point (e.g., the most upstream point of the system)'      
          type: number      
          x-ngsi:      
            type: Property      
        refPoint:      
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
          description: The reference point distance is measured from      
          x-ngsi:      
            type: Relationship      
      type: object      
      x-ngsi:      
        type: Property      
    rightSideSlope:      
      description: The slope of the right bank of the cross-section (for 'Trapezoidal' geometry). All units are accepted in CEFACT code      
      minimum: 0      
      type: number      
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
    specificConductivity:      
      description: Water conductivity at the cross-section      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    tag:      
      description: An optional text string used to qualify an item      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    turbidity:      
      description: Water turbidity at the cross-section      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI-LD Entity Type. It has to be CrossSection      
      enum:      
        - CrossSection      
      type: string      
      x-ngsi:      
        type: Property      
    waterFlow:      
      description: Water flow at the cross-section      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    waterLevel:      
      description: Water level at the cross-section      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    waterTemperature:      
      description: Water temperature at the cross-section      
      type: number      
      x-ngsi:      
        type: Property      
    waterVelocity:      
      description: Water Velocity at the cross-section      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/CrossSection/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/CrossSection/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### 断面 NGSI-v2 キー値の例    
以下は、JSON-LD形式のCrossSectionをkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CrossSection:id:COGE:70479090",  
  "type": "CrossSection",  
  "dateCreated": "1990-11-25T18:54:15Z",  
  "dateModified": "1999-04-24T10:03:17Z",  
  "source": "",  
  "name": "L3",  
  "alternateName": "Giona",  
  "description": "Giona 1",  
  "dataProvider": "",  
  "owner": [  
    "urn:ngsi-ld:CrossSection:items:ILNP:15826171",  
    "urn:ngsi-ld:CrossSection:items:RUEP:96519173"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:CrossSection:items:GEPQ:35001404",  
    "urn:ngsi-ld:CrossSection:items:YRBN:14719571"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      28.7415145,  
      -31.163341  
    ]  
  },  
  "address": {  
    "streetAddress": "",  
    "addressLocality": "",  
    "addressRegion": "",  
    "addressCountry": "",  
    "postalCode": "",  
    "postOfficeBoxNumber": "",  
    "areaServed": ""  
  },  
  "areaServed": "",  
  "attachedTo": "urn:ngsi-ld:CrossSection:attachedTo:CTHP:74683243",  
  "observedBy": "urn:ngsi-ld:CrossSection:observedBy:WJTI:74120377",  
  "tag": "",  
  "position": {  
    "distance": 864.6,  
    "refPoint": "urn:ngsi-ld:CrossSection:refPoint:JXFD:60487647"  
  },  
  "waterFlow": 12,  
  "waterVelocity": 0.082,  
  "waterTemperature": 9.6,  
  "turbidity": 11.8,  
  "specificConductivity": 260,  
  "waterLevel": 2.9,  
  "energyHead": 0.032,  
  "crossSectionGeometry": "Trapezoidal",  
  "bottomSlope": 0.02,  
  "leftSideSlope": 0.02,  
  "rightSideSlope": 0.02,  
  "bottomWidth": 5,  
  "diameter": 0,  
  "maxWaterDepth": 4,  
  "inheritsFrom": "urn:ngsi-ld:CrossSection:inheritsFrom:JXFD:60487647"  
}  
```  
</details>    
#### 断面 NGSI-v2 正規化例    
以下は、正規化された JSON-LD 形式の CrossSection の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CrossSection:id:COGE:70479090",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1990-11-25T18:54:15Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1999-04-24T10:03:17Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "L3"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Giona"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Giona 1"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": ""  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:CrossSection:items:ILNP:15826171",  
      "urn:ngsi-ld:CrossSection:items:RUEP:96519173"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:CrossSection:items:GEPQ:35001404",  
      "urn:ngsi-ld:CrossSection:items:YRBN:14719571"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        28.7415145,  
        -31.163341  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "",  
      "addressLocality": "",  
      "addressRegion": "",  
      "addressCountry": "",  
      "postalCode": "",  
      "postOfficeBoxNumber": "",  
      "areaServed": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": ""  
  },  
  "type": "CrossSection",  
  "attachedTo": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:CrossSection:attachedTo:CTHP:74683243"  
  },  
  "observedBy": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:CrossSection:observedBy:WJTI:74120377"  
  },  
  "tag": {  
    "type": "Text",  
    "value": ""  
  },  
  "position": {  
    "type": "StructuredValue",  
    "value": {  
      "distance": 864.6,  
      "refPoint": "urn:ngsi-ld:CrossSection:refPoint:JXFD:60487647"  
    }  
  },  
  "waterFlow": {  
    "type": "Number",  
    "value": 12  
  },  
  "waterVelocity": {  
    "type": "Number",  
    "value": 0.082  
  },  
  "waterTemperature": {  
    "type": "Number",  
    "value": 9.6  
  },  
  "turbidity": {  
    "type": "Number",  
    "value": 11.8  
  },  
  "specificConductivity": {  
    "type": "Number",  
    "value": 260  
  },  
  "waterLevel": {  
    "type": "Number",  
    "value": 2.9  
  },  
  "energyHead": {  
    "type": "Number",  
    "value": 0.032  
  },  
  "crossSectionGeometry": {  
    "type": "Text",  
    "value": "Trapezoidal"  
  },  
  "bottomSlope": {  
    "type": "Number",  
    "value": 0.02  
  },  
  "leftSideSlope": {  
    "type": "Number",  
    "value": 0.02  
  },  
  "rightSideSlope": {  
    "type": "Number",  
    "value": 0.02  
  },  
  "bottomWidth": {  
    "type": "Number",  
    "value": 5  
  },  
  "diameter": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maxWaterDepth": {  
    "type": "Number",  
    "value": 4  
  },  
  "inheritsFrom": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:CrossSection:inheritsFrom:JXFD:60487647"  
  }  
}  
```  
</details>    
#### 断面 NGSI-LD キー値の例    
以下は、JSON-LD形式のCrossSectionをkey-valuesとした例である。これはNGSI-LDと互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CrossSection:id:COGE:70479090",  
  "type": "CrossSection",  
  "address": {  
    "streetAddress": "",  
    "addressLocality": "",  
    "addressRegion": "",  
    "addressCountry": "",  
    "postalCode": "",  
    "postOfficeBoxNumber": "",  
    "areaServed": ""  
  },  
  "alternateName": "Giona",  
  "areaServed": "",  
  "attachedTo": "urn:ngsi-ld:CrossSection:attachedTo:CTHP:74683243",  
  "bottomSlope": 0.02,  
  "bottomWidth": 5,  
  "crossSectionGeometry": "Trapezoidal",  
  "dataProvider": "",  
  "dateCreated": "1990-11-25T18:54:15Z",  
  "dateModified": "1999-04-24T10:03:17Z",  
  "description": "Giona 1",  
  "diameter": 0,  
  "energyHead": 0.032,  
  "inheritsFrom": "urn:ngsi-ld:CrossSection:inheritsFrom:JXFD:60487647",  
  "leftSideSlope": 0.02,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      28.7415145,  
      -31.163341  
    ]  
  },  
  "maxWaterDepth": 4,  
  "name": "L3",  
  "observedBy": "urn:ngsi-ld:CrossSection:observedBy:WJTI:74120377",  
  "owner": [  
    "urn:ngsi-ld:CrossSection:items:ILNP:15826171",  
    "urn:ngsi-ld:CrossSection:items:RUEP:96519173"  
  ],  
  "position": {  
    "distance": 864.6,  
    "refPoint": "urn:ngsi-ld:CrossSection:refPoint:JXFD:60487647"  
  },  
  "rightSideSlope": 0.02,  
  "seeAlso": [  
    "urn:ngsi-ld:CrossSection:items:GEPQ:35001404",  
    "urn:ngsi-ld:CrossSection:items:YRBN:14719571"  
  ],  
  "source": "",  
  "specificConductivity": 260,  
  "tag": "",  
  "turbidity": 11.8,  
  "waterFlow": 12,  
  "waterLevel": 2.9,  
  "waterTemperature": 9.6,  
  "waterVelocity": 0.082,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 断面 NGSI-LD 正規化例    
以下は、正規化された JSON-LD 形式の CrossSection の例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:CrossSection:id:COGE:70479090",  
    "type": "CrossSection",  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "",  
            "addressLocality": "",  
            "addressRegion": "",  
            "addressCountry": "",  
            "postalCode": "",  
            "postOfficeBoxNumber": "",  
            "areaServed": ""  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "Giona"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "attachedTo": {  
        "type": "object",  
        "value": "urn:ngsi-ld:CrossSection:attachedTo:CTHP:74683243"  
    },  
    "bottomSlope": {  
        "type": "Property",  
        "value": 0.02  
    },  
    "bottomWidth": {  
        "type": "Property",  
        "value": 5  
    },  
    "crossSectionGeometry": {  
        "type": "Property",  
        "value": "Trapezoidal"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": ""  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1990-11-25T18:54:15Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1999-04-24T10:03:17Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Giona 1"  
    },  
    "diameter": {  
        "type": "Property",  
        "value": 0  
    },  
    "energyHead": {  
        "type": "Property",  
        "value": 0.032  
    },  
    "inheritsFrom": {  
        "type": "object",  
        "value": "urn:ngsi-ld:CrossSection:inheritsFrom:JXFD:60487647"  
    },  
    "leftSideSlope": {  
        "type": "Property",  
        "value": 0.02  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                28.7415145,  
                -31.163341  
            ]  
        }  
    },  
    "maxWaterDepth": {  
        "type": "Property",  
        "value": 4  
    },  
    "name": {  
        "type": "Property",  
        "value": "L3"  
    },  
    "observedBy": {  
        "type": "object",  
        "value": "urn:ngsi-ld:CrossSection:observedBy:WJTI:74120377"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:CrossSection:items:ILNP:15826171",  
            "urn:ngsi-ld:CrossSection:items:RUEP:96519173"  
        ]  
    },  
    "position": {  
        "type": "Property",  
        "value": {  
            "distance": 864.6,  
            "refPoint": "urn:ngsi-ld:CrossSection:refPoint:JXFD:60487647"  
        }  
    },  
    "rightSideSlope": {  
        "type": "Property",  
        "value": 0.02  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:CrossSection:items:GEPQ:35001404",  
            "urn:ngsi-ld:CrossSection:items:YRBN:14719571"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "specificConductivity": {  
        "type": "Property",  
        "value": 260  
    },  
    "tag": {  
        "type": "Property",  
        "value": ""  
    },  
    "turbidity": {  
        "type": "Property",  
        "value": 11.8  
    },  
    "waterFlow": {  
        "type": "Property",  
        "value": 12  
    },  
    "waterLevel": {  
        "type": "Property",  
        "value": 2.9  
    },  
    "waterTemperature": {  
        "type": "Property",  
        "value": 9.6  
    },  
    "waterVelocity": {  
        "type": "Property",  
        "value": 0.082  
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
