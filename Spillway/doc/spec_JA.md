<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ放水路  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/Spillway/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**このエンティティは、原水（開水路）システム管理領域で作成された一般的な Spillway の調和された記述を含んでいる。Spillway はジャンクションタイプのオブジェクトを表し、下流のダムや調節構造物からの放水を制御する**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `apronElevation[number]`: 放水路のすぐ上流にあるオージ放水路構造（P）の底面の標高です。  - `apronLength[number]`: 放水路底部の全長  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `controlCrossSection[*]`: Cross Section 型のエンティティの ID を示すリレーションシップで、Spillway 上の流量を制御するクロ スセクションを示す。  - `crestElevation[number]`: Spillway の頂部標高。ブロードクレスト型」、「オージー型」、「シャープクレスト型」のみ必要です。  - `crestLength[number]`: Spillwayの長さは、水が通過する全長と同じです。Broad-Crested", "Ogee", "Sharp-Crested" の場合のみ必要です。  - `curveDesignDischargeCoefficient[*]`: 設計流量係数(Co)をエプロン高さ(Co-P/Ho)の関数として表現したOpenChannelCurveエンティティのURIです。  - `curveDischargeCoefficient[*]`: 上流水頭 (H) と放水路形状の関数としての流量係数 (C) を表す OpenChannelCurve エンティティの URI です。例えば、放水路幅(C-H/L)上の上流頭部の関数としての放流係数、または C/Co-H/Ho のようなもの。  - `curveElevationDischarge[*]`: 水位(H)の関数として流量(Q)を表現するOpenChannelCurveエンティティのURIです。  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `designDischarge[number]`: 放水路の設計流量(Qo)  - `designDischargeCoefficient[number]`: 設計放電（Ho）に対するエネルギーロスの放電係数（Co）です。  - `designHead[number]`: オージースピルウェイ」の場合、スピルウェイが設計されている全上流エネルギーヘッド(Ho)  - `dischargeCoefficient[number]`: 放水路に水が入り、流れ、出る際のエネルギー損失に対する放水係数  - `id[*]`: エンティティの一意な識別子  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `maxFloodElevation[number]`: 放水路を通過できる水の最大標高。  - `name[string]`: このアイテムの名称です。  - `numberAbutments[number]`: オジー式放水路のアバットメントの数です。Ogee」タイプのみ。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `spillwayType[string]`: 放水路の種類を指定します。特定放水路」の場合、「標高-吐出量」曲線のみ必要です。Enum:'Broad-Crested, Ogee, Sharp-Crested, Specified Spillway'（ブロードクレスト、オージー、シャープクレスト、特定斜路）。  - `spillwayWidth[number]`: 放水路の幅(m)です。Broad-Crested」タイプのみ  - `tag[string]`: 項目を修飾するためのオプションのテキスト文字列  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI Entity Type。Spillwayである必要があります。  - `waterDischarge[number]`: 放水路からの流出量 (Q)  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `location`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Spillway:    
  description: 'This entity contains a harmonised description for a generic Spillway made for Raw-Water (Open Channels) System Management domain. Spillway represents a junction-type object, controlling the release of water from a dam or regulation structure downstream.'    
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
    apronElevation:    
      description: 'The elevation at the bottom of the ogee spillway structure (P), just upstream of the spillway.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    apronLength:    
      description: 'The total length of the spillway bottom'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    controlCrossSection:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of an entity of type Cross Section, indicating the cross section that controls the flow over the Spillway.'    
      x-ngsi:    
        type: Relationship    
    crestElevation:    
      description: 'The crest elevation of the Spillway. Required only for ''Broad-Crested'', ''Ogee'' and ''Sharp-Crested'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    crestLength:    
      description: 'The length of the Spillway equals to the total length through which water passes. Required only for ''Broad-Crested'', ''Ogee'' and ''Sharp-Crested'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    curveDesignDischargeCoefficient:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The URI of an OpenChannelCurve entity that represents the design discharge coefficient (Co) as a function of apron Elevation over design upstream head (Co-P/Ho).'    
      x-ngsi:    
        type: Relationship    
    curveDischargeCoefficient:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The URI of an OpenChannelCurve entity that represents the discharge coefficient (C) as a function of upstream head (H) and spillway geometry. For instance, discharge coefficient as a function of upstream head over spillway width (C-H/L), or C/Co-H/Ho.'    
      x-ngsi:    
        type: Relationship    
    curveElevationDischarge:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The URI of an OpenChannelCurve entity that represents discharge (Q) as a function of water elevation (H).'    
      x-ngsi:    
        type: Relationship    
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
    designDischarge:    
      description: 'The design discharge (Qo) of the Spillway'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: ' m^3/s.'    
    designDischargeCoefficient:    
      description: 'The discharge coefficient (Co) for energy losses for the design discharge (Ho).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    designHead:    
      description: 'The total upstream energy head for which the spillway is designed (Ho) for ''Ogee Spillway'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    dischargeCoefficient:    
      description: 'The discharge coefficient for energy losses as water enters, flows and exits the spillway'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: m^0.5/s.    
    id:    
      anyOf: &spillway_-_properties_-_owner_-_items_-_anyof    
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
    maxFloodElevation:    
      description: 'The maximum elevation of water that can pass the spillway.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numberAbutments:    
      description: 'The number of abutments of an ogee spillway. Only for ''Ogee'' type.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *spillway_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
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
    spillwayType:    
      description: 'The type of the spillway. In the case of “Specified Spillway”, only “Elevation – discharge” curve is required. Enum:''Broad-Crested, Ogee, Sharp-Crested, Specified Spillway''.'    
      enum:    
        - Broad-Crested    
        - Ogee    
        - Sharp-Crested    
        - 'Specified Spillway'    
      type: string    
      x-ngsi:    
        type: Property    
    spillwayWidth:    
      description: 'The width of the spillway (m). Only for ''Broad-Crested'' type'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters.    
    tag:    
      description: 'An optional text string used to qualify an item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity Type. It has to be Spillway.'    
      enum:    
        - Spillway    
      type: string    
      x-ngsi:    
        type: Property    
    waterDischarge:    
      description: 'The discharge over the spillway (Q)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: ' m^3/s'    
  required:    
    - id    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/Spillway/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/Spillway/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### Spillway NGSI-v2 key-value の例  
SpillwayをJSON-LD形式でkey-valuesにした例です。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Spillway:id:FFPG:06271993",  
  "type": "Spillway",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      60.3603485,  
      -129.682253  
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
  "dateCreated": "2020-10-12T04:27:47Z",  
  "dateModified": "2021-09-26T16:22:05Z",  
  "source": "",  
  "name": "SP01",  
  "alternateName": "SP01 - Thivae",  
  "description": "Spillway 01 - Thivae",  
  "dataProvider": "EYDAP",  
  "owner": [  
    "urn:ngsi-ld:Spillway:items:OFPV:04640010",  
    "urn:ngsi-ld:Spillway:items:BFAT:33357858"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Spillway:items:VLIF:47226224",  
    "urn:ngsi-ld:Spillway:items:BDSZ:68275691"  
  ],  
  "tag": "",  
  "spillwayType": "Ogee",  
  "crestElevation": 26.4,  
  "crestLength": 5,  
  "spillwayWidth": 5,  
  "numberAbutments": 2,  
  "apronElevation": 22,  
  "apronLength": 5,  
  "dischargeCoefficient": 5,  
  "designHead": 30.4,  
  "designDischarge": 20,  
  "designDischargeCoefficient": 0.4,  
  "maxFloodElevation": 4,  
  "waterDischarge": 9,  
  "controlCrossSection": "urn:ngsi-ld:Spillway:controlCrossSection:JXFD:60487647",  
  "curveElevationDischarge": "urn:ngsi-ld:Spillway:curveElevationDischarge:CBWI:21948924",  
  "curveDischargeCoefficient": "urn:ngsi-ld:Spillway:curveDischargeCoefficient:MWGU:81565938",  
  "curveDesignDischargeCoefficient": "urn:ngsi-ld:Spillway:curveDesignDischargeCoefficient:GIWE:80160975"  
}  
```  
</details>  
#### Spillway NGSI-v2 正規化例  
SpillwayをJSON-LD形式で正規化した例です。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Spillway:id:FFPG:06271993",  
  "type": "Spillway",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        60.3603485,  
        -129.682253  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
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
    "type": "Property",  
    "value": ""  
  },  
  "dateCreated":{  
      "type": "DateTime",  
      "value": "2020-10-12T04:27:47Z"  
  },  
  "dateModified": {  
      "type": "DateTime",  
      "value": "2021-09-26T16:22:05Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "SP01"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "SP01 - Thivae"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Spillway 01 - Thivae"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Spillway:items:OFPV:04640010",  
      "urn:ngsi-ld:Spillway:items:BFAT:33357858"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Spillway:items:VLIF:47226224",  
      "urn:ngsi-ld:Spillway:items:BDSZ:68275691"  
    ]  
  },  
  "tag": {  
    "type": "Text",  
    "value": ""  
  },  
  "spillwayType": {  
    "type": "Text",  
    "value": "Ogee"  
  },  
  "crestElevation": {  
    "type": "Number",  
    "value": 26.4  
  },  
  "crestLength": {  
    "type": "Number",  
    "value": 5  
  },  
  "spillwayWidth": {  
    "type": "Number",  
    "value": 5  
  },  
  "numberAbutments": {  
    "type": "Number",  
    "value": 2  
  },  
  "apronElevation": {  
    "type": "Number",  
    "value": 22  
  },  
  "apronLength": {  
    "type": "Number",  
    "value": 5  
  },  
  "dischargeCoefficient": {  
    "type": "Number",  
    "value": 5  
  },  
  "designHead": {  
    "type": "Number",  
    "value": 30.4  
  },  
  "designDischarge": {  
    "type": "Number",  
    "value": 20  
  },  
  "designDischargeCoefficient": {  
    "type": "Number",  
    "value": 0.4  
  },  
  "maxFloodElevation": {  
    "type": "Number",  
    "value": 4  
  },  
  "waterDischarge": {  
    "type": "Number",  
    "value": 9  
  },    
  "controlCrossSection": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Spillway:controlCrossSection:JXFD:60487647"  
  },  
  "curveElevationDischarge": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Spillway:curveElevationDischarge:CBWI:21948924"  
  },  
  "curveDischargeCoefficient": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Spillway:curveDischargeCoefficient:MWGU:81565938"  
  },  
  "curveDesignDischargeCoefficient": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Spillway:curveDesignDischargeCoefficient:GIWE:80160975"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### NGSI-LD キー値の例  
SpillwayをJSON-LD形式でkey-valuesにした例です。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータが返される。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Spillway:id:FFPG:06271993",  
    "type": "Spillway",  
    "address": {  
        "streetAddress": "",  
        "addressLocality": "",  
        "addressRegion": "",  
        "addressCountry": "",  
        "postalCode": "",  
        "postOfficeBoxNumber": "",  
        "areaServed": ""  
    },  
    "alternateName": "SP01 - Thivae",  
    "apronElevation": 22,  
    "apronLength": 5,  
    "areaServed": "",  
    "controlCrossSection": "urn:ngsi-ld:Spillway:controlCrossSection:JXFD:60487647",  
    "crestElevation": 26.4,  
    "crestLength": 5,  
    "curveDesignDischargeCoefficient": "urn:ngsi-ld:Spillway:curveDesignDischargeCoefficient:GIWE:80160975",  
    "curveDischargeCoefficient": "urn:ngsi-ld:Spillway:curveDischargeCoefficient:MWGU:81565938",  
    "curveElevationDischarge": "urn:ngsi-ld:Spillway:curveElevationDischarge:CBWI:21948924",  
    "dataProvider": "EYDAP",  
    "dateCreated": "2020-10-12T04:27:47Z",  
    "dateModified": "2021-09-26T16:22:05Z",  
    "description": "Spillway 01 - Thivae",  
    "designDischarge": 20,  
    "designDischargeCoefficient": 0.4,  
    "designHead": 30.4,  
    "dischargeCoefficient": 5,  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            60.3603485,  
            -129.682253  
        ]  
    },  
    "maxFloodElevation": 4,  
    "name": "SP01",  
    "numberAbutments": 2,  
    "owner": [  
        "urn:ngsi-ld:Spillway:items:OFPV:04640010",  
        "urn:ngsi-ld:Spillway:items:BFAT:33357858"  
    ],  
    "seeAlso": [  
        "urn:ngsi-ld:Spillway:items:VLIF:47226224",  
        "urn:ngsi-ld:Spillway:items:BDSZ:68275691"  
    ],  
    "source": "",  
    "spillwayType": "Ogee",  
    "spillwayWidth": 5,  
    "tag": "",  
    "waterDischarge": 9,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### NGSI-LDで正規化した例  
SpillwayをJSON-LD形式で正規化した例です。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Spillway:id:FFPG:06271993",  
    "type": "Spillway",  
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
        "value": "SP01 - Thivae"  
    },  
    "apronElevation": {  
        "type": "Property",  
        "value": 22  
    },  
    "apronLength": {  
        "type": "Property",  
        "value": 5  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "controlCrossSection": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Spillway:controlCrossSection:JXFD:60487647"  
    },  
    "crestElevation": {  
        "type": "Property",  
        "value": 26.4  
    },  
    "crestLength": {  
        "type": "Property",  
        "value": 5  
    },  
    "curveDesignDischargeCoefficient": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Spillway:curveDesignDischargeCoefficient:GIWE:80160975"  
    },  
    "curveDischargeCoefficient": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Spillway:curveDischargeCoefficient:MWGU:81565938"  
    },  
    "curveElevationDischarge": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Spillway:curveElevationDischarge:CBWI:21948924"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "EYDAP"  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-10-12T04:27:47Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-09-26T16:22:05Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Spillway 01 - Thivae"  
    },  
    "designDischarge": {  
        "type": "Property",  
        "value": 20  
    },  
    "designDischargeCoefficient": {  
        "type": "Property",  
        "value": 0.4  
    },  
    "designHead": {  
        "type": "Property",  
        "value": 30.4  
    },  
    "dischargeCoefficient": {  
        "type": "Property",  
        "value": 5  
    },  
    "location": {  
        "type": "Geoproperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                60.3603485,  
                -129.682253  
            ]  
        }  
    },  
    "maxFloodElevation": {  
        "type": "Property",  
        "value": 4  
    },  
    "name": {  
        "type": "Property",  
        "value": "SP01"  
    },  
    "numberAbutments": {  
        "type": "Property",  
        "value": 2  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:Spillway:items:OFPV:04640010",  
            "urn:ngsi-ld:Spillway:items:BFAT:33357858"  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:Spillway:items:VLIF:47226224",  
            "urn:ngsi-ld:Spillway:items:BDSZ:68275691"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "spillwayType": {  
        "type": "Property",  
        "value": "Ogee"  
    },  
    "spillwayWidth": {  
        "type": "Property",  
        "value": 5  
    },  
    "tag": {  
        "type": "Property",  
        "value": ""  
    },  
    "waterDischarge": {  
        "type": "Property",  
        "value": 9  
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
