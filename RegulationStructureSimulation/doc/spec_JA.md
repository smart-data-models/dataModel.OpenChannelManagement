<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ規制構造シミュレーション  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/RegulationStructureSimulation/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバル記述**このエンティティには、原水（開水路）システム管理領域における、規制構造シミュレーションのためのデータモデルの調和された記述が含まれる。  
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `endSimulationTime[date-time]`: シミュレーション終了時刻（ISO8601 UTC形式  - `equivalentSluiceOpening[number]`: 複数の水門がある場合の等価水門開度（異なる開度の平均値として推定される  - `estimatedGateDischargeCoefficient[number]`: 水門の校正排出係数  - `id[*]`: エンティティの一意識別子  - `initialConditions[array]`: シミュレーションのためにレギュレーション・ストラクチャーに適用される修正一式の説明  - `inputParameters[array]`: シミュレーションのためにレギュレーション・ストラクチャーに適用される修正一式の説明  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `modelError[number]`: 観測された放電量とシミュレートされた放電量の誤差の割合  - `modelledDischarge[number]`: シミュレーションモデルから推定される流出量  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `simulationOutput[array]`: 規制構造のシミュレーション結果一式の説明  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `spillwayFlow[number]`: 新しい総放流量に対する放水路放流量の比率  - `startSimulationTime[date-time]`: シミュレーション開始時刻（ISO8601 UTC形式  - `targetDischarge[number]`: ユーティリティ事業者によって定義された、水路に設置される望ましい放流量  - `type[string]`: NGSI-LDエンティティタイプ。RegulationStructureSimulationでなければならない。  <!-- /30-PropertiesList -->  
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
RegulationStructureSimulation:    
  description: 'This entity contains a harmonised description of a data model for regulation structure simulation, for Raw-Water (Open Channels) System Management domain.'    
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
    endSimulationTime:    
      description: Time of day in ISO8601 UTC format at which the simulation ends    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    equivalentSluiceOpening:    
      description: 'Equivalent sluice gate opening in the case of multiple sluice gates, estimated as the mean value of the different openings'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    estimatedGateDischargeCoefficient:    
      description: Calibrated discharge coefficient of the sluice gate    
      minimum: 0    
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
    initialConditions:    
      description: Description of the set of the modifications to be applied to the Regulation Structure for the simulation    
      items:    
        properties:    
          targetURI:    
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
            description: A relationship indicating the network component with a simulated property value    
            x-ngsi:    
              type: Relationship    
          value:    
            anyOf:    
              - type: string    
              - type: number    
              - type: boolean    
          waterAttribute:    
            description: 'Property: An attribute issued from the data models for Open Channel Management. It follows fully this data model and it could be a property or a relationship. It contains the values for specified properties, as derive from the simulation'    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    inputParameters:    
      description: Description of the set of the modifications to be applied to the Regulation Structure for the simulation    
      items:    
        properties:    
          targetURI:    
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
            description: A relationship indicating the network component with a simulated property value    
            x-ngsi:    
              type: Relationship    
          value:    
            anyOf:    
              - type: string    
              - type: number    
              - type: boolean    
          waterAttribute:    
            description: 'Property: An attribute issued from the data models for Open Channel Management. It follows fully this data model and it could be a property or a relationship. It contains the values for specified properties, as derive from the simulation'    
            type: string    
        type: object    
      type: array    
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
    modelError:    
      description: Percentage error between observed and simulated discharge    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    modelledDischarge:    
      description: Discharge estimated from the simulation model    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
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
    simulationOutput:    
      description: Description of the set of results of simulation of the regulation structure    
      items:    
        properties:    
          targetURI:    
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
            description: A relationship indicating the network component with a simulated property value    
            x-ngsi:    
              type: Relationship    
          value:    
            anyOf:    
              - type: string    
              - type: number    
              - type: boolean    
          waterAttribute:    
            description: 'Property: An attribute issued from the data models for Open Channel Management. It follows fully this data model and it could be a property or a relationship. It contains the values for specified properties, as derive from the simulation'    
            enum:    
              - gateOpening    
              - waterDischarge    
              - headDifference    
              - gateDischargeCoefficient    
              - waterFlow    
              - waterVelocity    
              - celerity    
              - travelDuration    
              - waterLevel    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    spillwayFlow:    
      description: Ratio of the spillway discharge to the new total discharge    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    startSimulationTime:    
      description: Time of day in ISO8601 UTC format at which the simulation begins    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    targetDischarge:    
      description: 'Desirable discharge to be established in the channel, defined by the utility’s operators'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI-LD Entity Type. It has to be RegulationStructureSimulation    
      enum:    
        - RegulationStructureSimulation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/RegulationStructureSimulation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/RegulationStructureSimulation/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### RegulationStructureSimulation NGSI-v2 キー値の例  
以下はRegulationStructureSimulationをJSON-LD形式でkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RegulationStructureSimulation:id:SCAU:96103454",  
  "type": "RegulationStructureSimulation",  
  "dateCreated": "2020-09-09T09:53:49Z",  
  "dateModified": "1978-02-07T04:20:08Z",  
  "source": "",  
  "name": "Regulation_Structure_Simulation_1",  
  "alternateName": "Regulation Structure Simulation 1",  
  "description": "Regulation Structure Simulation",  
  "dataProvider": "NTUA",  
  "owner": [  
    "urn:ngsi-ld:RegulationStructureSimulation:items:XYXQ:62496984",  
    "urn:ngsi-ld:RegulationStructureSimulation:items:ZHVH:90072950"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RegulationStructureSimulation:items:HQQG:85737160",  
    "urn:ngsi-ld:RegulationStructureSimulation:items:PCHL:09983431"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -27.391838,  
      -16.801411  
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
  "startSimulationTime": "2020-12-19T09:55:49Z",  
  "endSimulationTime": "2020-12-19T09:56:49Z",  
  "modelError": 0.004,  
  "targetDischarge": 14,  
  "modelledDischarge": 14,  
  "spillwayFlow": 0,  
  "estimatedGateDischargeCoefficient": 0.401,  
  "equivalentSluiceOpening": 490,  
  "simulationOutput": [  
    {  
      "waterAttribute": "waterLevel",  
      "value": 3.50,  
      "targetURI": "urn:ngsi-ld:CrossSection:CS01"  
    },  
    {  
      "waterAttribute": "gateOpening",  
      "value": 450,  
      "targetURI": "urn:ngsi-ld:SluiceGate:SG01"  
    }  
  ],  
  "inputParameters": [  
    {  
      "waterAttribute": "dischargeCoefficient",  
      "value": 1.9,  
      "targetURI": "urn:ngsi-ld:Spillway:SP01"  
    },  
    {  
      "waterAttribute": "gateDischargeCoefficient",  
      "value": 0.45,  
      "targetURI": "urn:ngsi-ld:SluiceGate:SG01"  
    }  
  ],  
  "initialConditions": [  
    {  
      "waterAttribute": "WaterFlow",  
      "value": 13.29,  
      "targetURI": "urn:ngsi-ld:CrossSection:CS01"  
    },  
    {  
      "waterAttribute": "Upstream Depth",  
      "value": 21,  
      "targetURI": "urn:ngsi-ld:CrossSection:CS02"  
    },  
    {  
      "waterAttribute": "GateOpening",  
      "value": 515,  
      "targetURI": "urn:ngsi-ld:SluiceGate:SG01"  
    }  
  ]  
}  
```  
</details>  
#### RegulationStructureSimulation NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のRegulationStructureSimulationの例です。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキスト・データを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RegulationStructureSimulation:id:SCAU:96103454",  
  "type": "RegulationStructureSimulation",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2020-09-09T09:53:49Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1978-02-07T04:20:08Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Regulation_Structure_Simulation_1"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Regulation Structure Simulation 1"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Regulation Structure Simulation"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "NTUA"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:RegulationStructureSimulation:items:XYXQ:62496984",  
      "urn:ngsi-ld:RegulationStructureSimulation:items:ZHVH:90072950"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:RegulationStructureSimulation:items:HQQG:85737160",  
      "urn:ngsi-ld:RegulationStructureSimulation:items:PCHL:09983431"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -27.391838,  
        -16.801411  
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
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": ""  
  },  
  "startSimulationTime": {  
    "type": "Datetime",  
    "value": "2020-12-19T09:55:49Z"  
  },  
  "endSimulationTime": {  
    "type": "Datetime",  
    "value": "2020-12-19T09:56:49Z"  
  },  
  "modelError": {  
    "type": "Number",  
    "value": 0.004  
  },  
  "targetDischarge": {  
    "type": "Number",  
    "value": 14  
  },  
  "modelledDischarge": {  
    "type": "Number",  
    "value": 14  
  },  
  "spillwayFlow": {  
    "type": "Number",  
    "value": 0  
  },  
  "estimatedGateDischargeCoefficient": {  
    "type": "Number",  
    "value": 0.401  
  },  
  "equivalentSluiceOpening": {  
    "type": "Number",  
    "value": 490  
  },  
  "simulationOutput": {  
    "type": "array",  
    "value": [  
      {  
        "waterAttribute": "waterLevel",  
        "value": 3.50,  
        "targetURI": "urn:ngsi-ld:CrossSection:CS01"  
      },  
      {  
        "waterAttribute": "gateOpening",  
        "value": 450,  
        "targetURI": "urn:ngsi-ld:SluiceGate:SG01"  
      }  
    ]  
  },  
  "inputParameters": {  
    "type": "array",  
    "value": [  
      {  
        "waterAttribute": "dischargeCoefficient",  
        "value": 1.9,  
        "targetURI": "urn:ngsi-ld:Spillway:SP01"  
      },  
      {  
        "waterAttribute": "gateDischargeCoefficient",  
        "value": 0.45,  
        "targetURI": "urn:ngsi-ld:SluiceGate:SG01"  
      }  
    ]  
  },  
  "initialConditions": {  
    "type": "array",  
    "value": [  
      {  
        "waterAttribute": "WaterFlow",  
        "value": 13.29,  
        "targetURI": "urn:ngsi-ld:CrossSection:CS01"  
      },  
      {  
        "waterAttribute": "Upstream Depth",  
        "value": 21,  
        "targetURI": "urn:ngsi-ld:CrossSection:CS02"  
      },  
      {  
        "waterAttribute": "GateOpening",  
        "value": 515,  
        "targetURI": "urn:ngsi-ld:SluiceGate:SG01"  
      }  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### 規制構造シミュレーション NGSI-LD キー値の例  
以下はRegulationStructureSimulationをJSON-LD形式でkey-valuesとして表した例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RegulationStructureSimulation:id:SCAU:96103454",  
    "type": "RegulationStructureSimulation",  
    "address": {  
        "streetAddress": "",  
        "addressLocality": "",  
        "addressRegion": "",  
        "addressCountry": "",  
        "postalCode": "",  
        "postOfficeBoxNumber": ""  
    },  
    "alternateName": "Regulation Structure Simulation 1",  
    "areaServed": "",  
    "dataProvider": "NTUA",  
    "dateCreated": "2020-09-09T09:53:49Z",  
    "dateModified": "1978-02-07T04:20:08Z",  
    "description": "Regulation Structure Simulation",  
    "endSimulationTime": "2020-12-19T09:56:49Z",  
    "equivalentSluiceOpening": 490,  
    "estimatedGateDischargeCoefficient": 0.401,  
    "initialConditions": [  
        {  
            "waterAttribute": "WaterFlow",  
            "value": 13.29,  
            "targetURI": "urn:ngsi-ld:CrossSection:CS01"  
        },  
        {  
            "waterAttribute": "Upstream Depth",  
            "value": 21,  
            "targetURI": "urn:ngsi-ld:CrossSection:CS02"  
        },  
        {  
            "waterAttribute": "GateOpening",  
            "value": 515,  
            "targetURI": "urn:ngsi-ld:SluiceGate:SG01"  
        }  
    ],  
    "inputParameters": [  
        {  
            "waterAttribute": "dischargeCoefficient",  
            "value": 1.9,  
            "targetURI": "urn:ngsi-ld:Spillway:SP01"  
        },  
        {  
            "waterAttribute": "gateDischargeCoefficient",  
            "value": 0.45,  
            "targetURI": "urn:ngsi-ld:SluiceGate:SG01"  
        }  
    ],  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -27.391838,  
            -16.801411  
        ]  
    },  
    "modelError": 0.004,  
    "modelledDischarge": 14,  
    "name": "Regulation_Structure_Simulation_1",  
    "owner": [  
        "urn:ngsi-ld:RegulationStructureSimulation:items:XYXQ:62496984",  
        "urn:ngsi-ld:RegulationStructureSimulation:items:ZHVH:90072950"  
    ],  
    "seeAlso": [  
        "urn:ngsi-ld:RegulationStructureSimulation:items:HQQG:85737160",  
        "urn:ngsi-ld:RegulationStructureSimulation:items:PCHL:09983431"  
    ],  
    "simulationOutput": [  
        {  
            "waterAttribute": "waterLevel",  
            "value": 3.5,  
            "targetURI": "urn:ngsi-ld:CrossSection:CS01"  
        },  
        {  
            "waterAttribute": "gateOpening",  
            "value": 450,  
            "targetURI": "urn:ngsi-ld:SluiceGate:SG01"  
        }  
    ],  
    "source": "",  
    "spillwayFlow": 0,  
    "startSimulationTime": "2020-12-19T09:55:49Z",  
    "targetDischarge": 14,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### 規制構造シミュレーション NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のRegulationStructureSimulationの例です。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RegulationStructureSimulation:id:SCAU:96103454",  
    "type": "RegulationStructureSimulation",  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "",  
            "addressLocality": "",  
            "addressRegion": "",  
            "addressCountry": "",  
            "postalCode": "",  
            "postOfficeBoxNumber": ""  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "Regulation Structure Simulation 1"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "NTUA"  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-09-09T09:53:49Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1978-02-07T04:20:08Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Regulation Structure Simulation"  
    },  
    "endSimulationTime": {  
        "type": "Property",  
        "value": {  
            "@type": "Datetime",  
            "@value": "2020-12-19T09:56:49Z"  
        }  
    },  
    "equivalentSluiceOpening": {  
        "type": "Property",  
        "value": 490  
    },  
    "estimatedGateDischargeCoefficient": {  
        "type": "Property",  
        "value": 0.401  
    },  
    "initialConditions": {  
        "type": "Property",  
        "value": [  
            {  
                "waterAttribute": "WaterFlow",  
                "value": 13.29,  
                "targetURI": "urn:ngsi-ld:CrossSection:CS01"  
            },  
            {  
                "waterAttribute": "Upstream Depth",  
                "value": 21,  
                "targetURI": "urn:ngsi-ld:CrossSection:CS02"  
            },  
            {  
                "waterAttribute": "GateOpening",  
                "value": 515,  
                "targetURI": "urn:ngsi-ld:SluiceGate:SG01"  
            }  
        ]  
    },  
    "inputParameters": {  
        "type": "Property",  
        "value": [  
            {  
                "waterAttribute": "dischargeCoefficient",  
                "value": 1.9,  
                "targetURI": "urn:ngsi-ld:Spillway:SP01"  
            },  
            {  
                "waterAttribute": "gateDischargeCoefficient",  
                "value": 0.45,  
                "targetURI": "urn:ngsi-ld:SluiceGate:SG01"  
            }  
        ]  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -27.391838,  
                -16.801411  
            ]  
        }  
    },  
    "modelError": {  
        "type": "Property",  
        "value": 0.004  
    },  
    "modelledDischarge": {  
        "type": "Property",  
        "value": 14  
    },  
    "name": {  
        "type": "Property",  
        "value": "Regulation_Structure_Simulation_1"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:RegulationStructureSimulation:items:XYXQ:62496984",  
            "urn:ngsi-ld:RegulationStructureSimulation:items:ZHVH:90072950"  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:RegulationStructureSimulation:items:HQQG:85737160",  
            "urn:ngsi-ld:RegulationStructureSimulation:items:PCHL:09983431"  
        ]  
    },  
    "simulationOutput": {  
        "type": "Property",  
        "value": [  
            {  
                "waterAttribute": "waterLevel",  
                "value": 3.5,  
                "targetURI": "urn:ngsi-ld:CrossSection:CS01"  
            },  
            {  
                "waterAttribute": "gateOpening",  
                "value": 450,  
                "targetURI": "urn:ngsi-ld:SluiceGate:SG01"  
            }  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "spillwayFlow": {  
        "type": "Property",  
        "value": 0  
    },  
    "startSimulationTime": {  
        "type": "Property",  
        "value": {  
            "@type": "Datetime",  
            "@value": "2020-12-19T09:55:49Z"  
        }  
    },  
    "targetDischarge": {  
        "type": "Property",  
        "value": 14  
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
