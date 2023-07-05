<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティOpenChannelCurve  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/OpenChannelCurve/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**このエンティティは、原水（開放水路）システム管理領域のために作られた汎用曲線の調和された記述を含んでいる。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `curveType[string]`: 放水路や調節構造物の曲線の種類。を表す曲線とすることができる。1) 相対堰開度（a/H、a：水門開度、H：上流頭）の関数としての放流係数（C）、2) 水位（H）の関数としての放流量（Q）、3) 設計放流係数（Co）を表す曲線とすることができる。(2) 水位(H)の関数としての流量(Q)、(3) P/Hoの関数としての設計流量係数（Co）、ここでPはOGEE放水路のエプロン高、Hoは設計上昇流頭、4）H/Lの関数としての流量係数（C）、ここでHは上流頭、LはBROAD-CRESTED放水路の脚長、5） C/Co - H/Ho関数、があります。Enum:'C-a/H, H-Q, Co-P/Ho, C-H/L, C/Co-H/Ho'.  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `tag[string]`: 項目を修飾するためのオプションのテキスト文字列  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI エンティティタイプ。OpenChannelCurveでなければならない。  - `xData[array]`: カーブのデータポイントをX個にする。  - `yData[array]`: 曲線のYデータ点。  <!-- /30-PropertiesList -->  
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
OpenChannelCurve:    
  description: 'This entity contains a harmonised description of a generic curve made for Raw-Water (Open Channels) System Management domain.'    
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
    curveType:    
      description: 'Type of curve for spillways and regulation structures. It can be a curve representing: 1) the discharge coefficient (C) as a function of relative weir opening (a/H, a: sluice-gate opening, H: upstream head), 2) the discharge (Q) as a function of the water elevation (H), 3) the design discharge coefficient (Co) as a function of P/Ho, where P is the apron elevation of the OGEE spillway and Ho the design upstrean head, 4) discharge coefficient (C) as a function of H/L, where H is the upstream head and L the legnth of a BROAD-CRESTED spillway, 5) the function C/Co - H/Ho. Enum:''C-a/H, H-Q, Co-P/Ho, C-H/L, C/Co-H/Ho'''    
      enum:    
        - a/H-C    
        - H-Q    
        - Co-P/Ho    
        - C-H/L    
        - C/Co-H/Ho    
      type: string    
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
    id:    
      anyOf: &openchannelcurve_-_properties_-_owner_-_items_-_anyof    
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
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *openchannelcurve_-_properties_-_owner_-_items_-_anyof    
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
    tag:    
      description: 'An optional text string used to qualify an item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity Type. It has to be OpenChannelCurve'    
      enum:    
        - OpenChannelCurve    
      type: string    
      x-ngsi:    
        type: Property    
    xData:    
      description: 'X data points for the curve.'    
      items:    
        type: number    
      type: array    
      x-ngsi:    
        type: Property    
    yData:    
      description: 'Y data points for the curve.'    
      items:    
        type: number    
      type: array    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/OpenChannelCurve/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/OpenChannelCurve/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### OpenChannelCurve NGSI-v2 key-value の例です。  
ここでは、OpenChannelCurveをJSON-LD形式でkey-valuesにした例を示します。これは `options=keyValues` を使ったときに NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータが返される。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelCurve:id:FMCV:30717942",  
  "type": "OpenChannelCurve",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -71.481035,  
      -148.255307  
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
  "dateCreated": "2003-09-09T04:19:40Z",  
  "dateModified": "2019-04-13T13:45:31Z",  
  "source": "",  
  "name": "Curve_1",  
  "alternateName": "",  
  "description": "Open Channel Curve for a/H ~ C",  
  "dataProvider": "NTUA",  
  "owner": [  
    "urn:ngsi-ld:OpenChannelCurve:items:EXUV:99745990",  
    "urn:ngsi-ld:OpenChannelCurve:items:HXOV:60683026"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:OpenChannelCurve:items:IZFN:20714900",  
    "urn:ngsi-ld:OpenChannelCurve:items:RDSS:63995745"  
  ],  
  "tag": "a/H ~ C curve",  
  "curveType": "a/H ~ C",  
  "xData": [  
    0.001,  
    0.1,  
    0.2,  
    0.3,  
    0.4,  
    0.5,  
    0.6,  
    0.7  
  ],  
  "yData": [  
    0.61,  
    0.5930,  
    0.5942,  
    0.5988,  
    0.6070,  
    0.6209,  
    0.6395,  
    0.6628  
  ]  
}  
```  
</details>  
#### OpenChannelCurve NGSI-v2 正規化例  
OpenChannelCurveを正規化したJSON-LD形式の例です。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelCurve:id:FMCV:30717942",  
  "type": "OpenChannelCurve",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -71.481035,  
        -148.255307  
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
    "type": "Text",  
    "value": ""  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2003-09-09T04:19:40Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2019-04-13T13:45:31Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Curve_1"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "Open Channel Curve for a/H-C"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "NTUA"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:OpenChannelCurve:items:EXUV:99745990",  
      "urn:ngsi-ld:OpenChannelCurve:items:HXOV:60683026"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:OpenChannelCurve:items:IZFN:20714900",  
      "urn:ngsi-ld:OpenChannelCurve:items:RDSS:63995745"  
    ]  
  },  
  "tag": {  
    "type": "Text",  
    "value": "a/H-C curve"  
  },  
  "curveType": {  
    "type": "Text",  
    "value": "a/H-C"  
  },  
  "xData": {  
    "type": "array",  
    "value": [  
      0.001,  
      0.1,  
      0.2,  
      0.3,  
      0.4,  
      0.5,  
      0.6,  
      0.7  
    ]  
  },  
  "yData": {  
    "type": "array",  
    "value": [  
      0.61,  
      0.5930,  
      0.5942,  
      0.5988,  
      0.6070,  
      0.6209,  
      0.6395,  
      0.6628  
    ]  
  }  
}  
```  
</details>  
#### OpenChannelCurve NGSI-LD key-value の例  
OpenChannelCurveをJSON-LD形式でkey-valuesにした例です。これは `options=keyValues` を使った場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータが返される。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:OpenChannelCurve:id:FMCV:30717942",  
    "type": "OpenChannelCurve",  
    "address": {  
        "streetAddress": "",  
        "addressLocality": "",  
        "addressRegion": "",  
        "addressCountry": "",  
        "postalCode": "",  
        "postOfficeBoxNumber": "",  
        "areaServed": ""  
    },  
    "alternateName": "",  
    "areaServed": "",  
    "curveType": "a/H ~ C",  
    "dataProvider": "NTUA",  
    "dateCreated": "2003-09-09T04:19:40Z",  
    "dateModified": "2019-04-13T13:45:31Z",  
    "description": "Open Channel Curve for a/H ~ C",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -71.481035,  
            -148.255307  
        ]  
    },  
    "name": "Curve_1",  
    "owner": [  
        "urn:ngsi-ld:OpenChannelCurve:items:EXUV:99745990",  
        "urn:ngsi-ld:OpenChannelCurve:items:HXOV:60683026"  
    ],  
    "seeAlso": [  
        "urn:ngsi-ld:OpenChannelCurve:items:IZFN:20714900",  
        "urn:ngsi-ld:OpenChannelCurve:items:RDSS:63995745"  
    ],  
    "source": "",  
    "tag": "a/H ~ C curve",  
    "xData": [  
        0.001,  
        0.1,  
        0.2,  
        0.3,  
        0.4,  
        0.5,  
        0.6,  
        0.7  
    ],  
    "yData": [  
        0.61,  
        0.593,  
        0.5942,  
        0.5988,  
        0.607,  
        0.6209,  
        0.6395,  
        0.6628  
    ],  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### OpenChannelCurve NGSI-LD 正規化例  
OpenChannelCurveをJSON-LD形式で正規化した例を示します。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:OpenChannelCurve:id:FMCV:30717942",  
    "type": "OpenChannelCurve",  
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
        "value": ""  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "curveType": {  
        "type": "Property",  
        "value": "a/H ~ C"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "NTUA"  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2003-09-09T04:19:40Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2019-04-13T13:45:31Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Open Channel Curve for a/H ~ C"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -71.481035,  
                -148.255307  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Curve_1"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:OpenChannelCurve:items:EXUV:99745990",  
            "urn:ngsi-ld:OpenChannelCurve:items:HXOV:60683026"  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:OpenChannelCurve:items:IZFN:20714900",  
            "urn:ngsi-ld:OpenChannelCurve:items:RDSS:63995745"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "tag": {  
        "type": "Property",  
        "value": "a/H ~ C curve"  
    },  
    "xData": {  
        "type": "Property",  
        "value": [  
            0.001,  
            0.1,  
            0.2,  
            0.3,  
            0.4,  
            0.5,  
            0.6,  
            0.7  
        ]  
    },  
    "yData": {  
        "type": "Property",  
        "value": [  
            0.61,  
            0.593,  
            0.5942,  
            0.5988,  
            0.607,  
            0.6209,  
            0.6395,  
            0.6628  
        ]  
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
