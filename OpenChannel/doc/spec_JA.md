<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティOpenChannel  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/OpenChannel/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**このエンティティは、生水(オープンチャンネル)システム管理領域のために作られた汎用チャンネルの調和された記述を含んでいます。  
バージョン: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bottomSlope[number]`: 水路の底面勾配。単位はすべてCEFACTコードで受け付けています。  - `bottomWidth[number]`: チャンネルの底幅 (「台形」ジオメトリの場合)。すべての単位はCEFACTコードで受け入れられます。  - `celerity[number]`: 水門の開閉後に水路に沿って伝播するサージを速度で表したもの。  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `diameter[number]`: 円形チャネルの直径。すべての単位はCEFACTコードで受け付けています。  - `downstreamNode[*]`: チャネルが終了する下流ノード（例：Junction、Regulation Structure）のIDを示す関係である。  - `flowType[string]`: 水路の流れの種類を定義するテキスト。Enum:'Free-Surface flow'.  - `geometryType[string]`: 水路の形状。Enum:'Trapezoidal, Circular'].  - `id[*]`: エンティティの一意な識別子  - `leftSideSlope[number]`: 水路の左岸の勾配（「台形」ジオメトリの場合）。すべての単位はCEFACTコードで受け入れられます。  - `length[number]`: チャンネルの長さ。単位はすべてCEFACTコードで受け付けます。  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `maxWaterDepth[number]`: 水路の最大許容水深。単位はすべてCEFACTコードで受け付けます。  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `rightSideSlope[number]`: 水路の右岸の勾配（「台形」ジオメトリの場合）。すべての単位はCEFACTコードで受け入れられます。  - `roughnessCoefficient[number]`: マニングの粗度係数を表す。  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `tag[string]`: 項目を修飾するためのオプションのテキスト文字列  . Model: [https://schema.org/Text](https://schema.org/Text)- `travelDuration[number]`: 下流側のノード（Regulation Structure）から上流側のノードに伝わるサージの継続時間。  - `type[string]`: NGSI-LD Entity Type。OpenChannelでなければならない。  - `upstreamNode[*]`: チャネルが始まる上流ノード（例：Junction、Regulation Structure）のIDを示す関係である。  - `waterLoss[number]`: 水路からの漏水／損失-水路の流量に対する割合または数値（流量）。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OpenChannel:    
  description: 'This entity contains a harmonised description of a generic Channel made for Raw-Water (Open Channels) System Management domain.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bottomSlope:    
      description: 'The bottom slope of the channel. All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    bottomWidth:    
      description: 'The bottom width of the channel (for ''Trapezoidal'' geometry). All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    celerity:    
      description: 'Velocity of a surge propagated along the channel after the opening or close of a sluice gate.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    diameter:    
      description: 'The diameter of a circular channel. All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    downstreamNode:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of the downstream node (e.g., Junction, Regulation Structure), where the channel ends.'    
      x-ngsi:    
        type: Relationship    
    flowType:    
      description: 'Text defining the type of flow in the channel. Enum:''Free-Surface flow''.'    
      enum:    
        - 'Free-Surface flow'    
      type: string    
      x-ngsi:    
        type: Property    
    geometryType:    
      description: 'The geometry of the channel. Enum:''Trapezoidal, Circular''].'    
      enum:    
        - Circular    
        - Trapezoidal    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &openchannel_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    leftSideSlope:    
      description: 'The slope of the left bank of the channel (for ''Trapezoidal'' geometry). All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    length:    
      description: 'The length of the channel. All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    maxWaterDepth:    
      description: 'The maximum allowable water depth in the channel. All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *openchannel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    rightSideSlope:    
      description: 'The slope of the right bank of the channel (for ''Trapezoidal'' geometry). All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    roughnessCoefficient:    
      description: 'The Manning’s roughness coefficient.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    tag:    
      description: 'An optional text string used to qualify an item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    travelDuration:    
      description: 'The duration of the surge travelling from the downstream node (i.e., Regulation Structure) to the upstream node.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI-LD Entity Type. it has to be OpenChannel'    
      enum:    
        - OpenChannel    
      type: string    
      x-ngsi:    
        type: Property    
    upstreamNode:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of the upstream node (e.g., Junction, Regulation Structure), where the channel begins.'    
      x-ngsi:    
        type: Relationship    
    waterLoss:    
      description: 'Water leakages/losses from the channel - percentage of flow of the channel or a number (flow).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/OpenChannel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/Channel/schema.json    
  x-model-tags: ""    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### OpenChannel NGSI-v2 key-value の例です。  
ここでは、OpenChannelをJSON-LD形式でkey-valuesにした例を示します。これは、`options=keyValues`を使ったときにNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
以下は、正規化されたJSON-LD形式のOpenChannelの例です。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:Channel:items:ZOOU:49614637",  
      "urn:ngsi-ld:Channel:items:ODUZ:33451005"  
    ]  
  },  
  "seeAlso": {  
    "type": "Array",  
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
    "type": "object",  
    "value": "urn:ngsi-ld:Channel:downstreamNode:DQUS:63966588"  
  },  
  "upstreamNode": {  
    "type": "Relationship",  
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
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### OpenChannel NGSI-LD キー値の例  
ここでは、OpenChannelをJSON-LD形式でkey-valuesにした例を示します。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
OpenChannelをJSON-LD形式で正規化した例を示します。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
