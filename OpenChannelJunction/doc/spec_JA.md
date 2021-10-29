エンティティOpenChannelJunction  
=========================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/OpenChannelJunction/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**このエンティティは、Raw-Water (Open Channels) System Managementドメインのために作られた一般的なジャンクションの調和された記述を含む。ジャンクションは、チャネルの特性が変化する場所を定義し、2つ以上のチャネルが一緒になったり分かれたり、水の量がシステムに取り込まれたり挿入されたりします。  
バージョン: 0.0.1  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `downstreamNode`: チャネルが終了する下流のノード（Junction、Regulation Structureなど）のIDを示す関係。  - `id`: エンティティのユニークな識別子  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `name`: このアイテムの名前です。  - `observedBy`: 原水の特性をモニターする装置のIDとの関係  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `position`: 残りの要素との距離や関係性に関する情報を提供するオブジェクト。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `tag`: アイテムを修飾するための任意のテキスト文字列  - `type`: NGSI Entity Type. OpenChannelJunctionである必要があります。  - `uniqueName`: ジャンクションの名前です。  - `upstreamNode`: チャネルの始点となる上流のノード（Junction、Regulation Structureなど）のIDを示す関係です。  - `waterInflow`: ジャンクションに挿入された水流  - `waterOutflow`: ジャンクションから抽出された水流、または別の水源に転用された水流    
必須項目  
- `id`  - `type`  ## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OpenChannelJunction:    
  description: 'This entity contains a harmonised description of a generic Junction made for Raw-Water (Open Channels) System Management domain. A Junction defines a location where the characteristics of the channel changes, two or more channels come together or split apart, amounts of water are abstracted or inserted to the system etc.'    
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
    id:    
      anyOf: &openchanneljunction_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observedBy:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship to the ID of the device that monitors raw-water properties'    
      x-ngsi:    
        model: https://smart-data-models.github.io/dataModel.Device/device-schema.json    
        type: Relationship    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *openchanneljunction_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    position:    
      description: 'Object providing information about the distance with the rest of the elements and a relationship with them.'    
      properties:    
        distance:    
          description: 'Property. The distance between this Entity and a reference point (e.g., the most upstream point of the system). Units: ''Km'''    
          type: number    
        refPoint:    
          anyOf:    
            - description: 'Property. Identifier format of any NGSI entity.'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity.'    
              format: uri    
              type: string    
          description: 'Relationship. The reference point distance is measured from.'    
      type: object    
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
      description: 'NGSI Entity Type. it has to be OpenChannelJunction'    
      enum:    
        - OpenChannelJunction    
      type: string    
      x-ngsi:    
        type: Property    
    uniqueName:    
      description: 'The name of the junction.'    
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
    waterInflow:    
      description: 'Water flow inserted to the junction'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: m3/s    
    waterOutflow:    
      description: 'Water flow abstracted from the junction or diverted to another source'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: m3/s    
  required:    
    - id    
    - type    
  type: object    
  version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### OpenChannelJunction NGSI-v2 のキーバリューの例。  
OpenChannelJunctionをkey-valuesとしてJSON-LD形式で記述した例を示します。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelJunction:id:PTOM:78370074",  
  "type": "OpenChannelJunction",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -65.2981945,  
      -22.649102  
    ]  
  },  
  "address": {  
    "streetAddress": "",  
    "addressLocality": "",  
    "addressRegion": "",  
    "addressCountry": "",  
    "postalCode": "",  
    "postOfficeBoxNumber": ""  
  },  
  "areaServed": "",  
  "dateCreated": "1983-10-11T21:04:39Z",  
  "dateModified": "1982-03-03T08:37:57Z",  
  "source": "",  
  "name": "J1",  
  "alternateName": "Thivae",  
  "dataProvider": "EYDAP",  
  "owner": [  
    "urn:ngsi-ld:OpenChannelJunction:items:QPEH:03184806",  
    "urn:ngsi-ld:OpenChannelJunction:items:PUHR:34031741"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:OpenChannelJunction:items:KTWJ:61564622",  
    "urn:ngsi-ld:OpenChannelJunction:items:JOMY:24566116"  
  ],  
  "position": {  
    "distance": 160.6,  
    "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647",  
    "downstreamNode": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924",  
    "upstreamNode": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938",  
    "observedBy": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975",  
    "uniqueName": "J1",  
    "tag": "",  
    "waterOutflow": 0.12,  
    "waterInflow": 0.15  
  }  
}  
```  
#### OpenChannelJunction NGSI-v2 正規化例  
ここでは、正規化されたJSON-LD形式のOpenChannelJunctionの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelJunction:id:PTOM:78370074",  
  "type": "OpenChannelJunction",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -65.2981945,  
        -22.649102  
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
    "value": "1983-10-11T21:04:39Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1982-03-03T08:37:57Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "J1"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Thivae"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Open Channel Junction"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:OpenChannelJunction:items:QPEH:03184806",  
      "urn:ngsi-ld:OpenChannelJunction:items:PUHR:34031741"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:OpenChannelJunction:items:KTWJ:61564622",  
      "urn:ngsi-ld:OpenChannelJunction:items:JOMY:24566116"  
    ]  
  },  
  "position": {  
    "type": "StructuredValue",  
    "value": {  
      "distance": 160.6,  
      "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647"  
    }  
  },  
  "downstreamNode": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924"  
  },  
  "upstreamNode": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938"  
  },  
  "observedBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975"  
  },  
  "uniqueName": {  
    "type": "Text",  
    "value": "J1"  
  },  
  "tag": {  
    "type": "Text",  
    "value": ""  
  },  
  "waterOutflow": {  
    "type": "Number",  
    "value": 0.12  
  },  
  "waterInflow": {  
    "type": "Number",  
    "value": 0.15  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### OpenChannelJunction NGSI-LDのキーバリューの例。  
ここでは、OpenChannelJunctionをkey-valuesとしてJSON-LD形式にした例を紹介します。これは、`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelJunction:id:PTOM:78370074",  
  "type": "OpenChannelJunction",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -65.2981945,  
      -22.649102  
    ]  
  },  
  "address": {  
    "streetAddress": "",  
    "addressLocality": "",  
    "addressRegion": "",  
    "addressCountry": "",  
    "postalCode": "",  
    "postOfficeBoxNumber": ""  
  },  
  "areaServed": "",  
  "dateCreated": "1983-10-11T21:04:39Z",  
  "dateModified": "1982-03-03T08:37:57Z",  
  "source": "",  
  "name": "J1",  
  "alternateName": "Thivae",  
  "dataProvider": "EYDAP",  
  "owner": [  
    "urn:ngsi-ld:OpenChannelJunction:items:QPEH:03184806",  
    "urn:ngsi-ld:OpenChannelJunction:items:PUHR:34031741"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:OpenChannelJunction:items:KTWJ:61564622",  
    "urn:ngsi-ld:OpenChannelJunction:items:JOMY:24566116"  
  ],  
  "position": {  
    "distance": 160.6,  
    "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647",  
    "downstreamNode": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924",  
    "upstreamNode": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938",  
    "observedBy": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975",  
    "uniqueName": "J1",  
    "tag": "",  
    "waterOutflow": 0.12,  
    "waterInflow": 0.15  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### OpenChannelJunction NGSI-LDの正規化例  
OpenChannelJunctionを正規化したJSON-LD形式の例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelJunction:id:PTOM:78370074",  
  "type": "OpenChannelJunction",  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -65.2981945,  
        -22.649102  
      ]  
    }  
  },  
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
  "areaServed": {  
    "type": "Property",  
    "value": ""  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1983-10-11T21:04:39Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1982-03-03T08:37:57Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "J1"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Thivae"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Open Channel Junction"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:OpenChannelJunction:items:QPEH:03184806",  
      "urn:ngsi-ld:OpenChannelJunction:items:PUHR:34031741"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:OpenChannelJunction:items:KTWJ:61564622",  
      "urn:ngsi-ld:OpenChannelJunction:items:JOMY:24566116"  
    ]  
  },  
  "position": {  
    "type": "Property",  
    "value": {  
      "distance": 160.6,  
      "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647"  
    }  
  },  
  "downstreamNode": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924"  
  },  
  "upstreamNode": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938"  
  },  
  "observedBy": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975"  
  },  
  "uniqueName": {  
    "type": "Property",  
    "value": "J1"  
  },  
  "tag": {  
    "type": "Property",  
    "value": ""  
  },  
  "waterOutflow": {  
    "type": "Property",  
    "value": 0.12  
  },  
  "waterInflow": {  
    "type": "Property",  
    "value": 0.15  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
