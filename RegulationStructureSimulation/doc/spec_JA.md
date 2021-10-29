エンティティRegulationStructureSimulation  
===================================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/RegulationStructureSimulation/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**このエンティティには、原水（オープンチャンネル）システム管理ドメインの規制構造シミュレーションのためのデータモデルの調和された記述が含まれています。  
バージョン: 0.0.1  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `endSimulationTime`: シミュレーションを終了する時刻（ISO8601 UTC形式）。  - `equivalentSluiceOpening`: 複数の水門がある場合の等価な水門の開度で、異なる開度の平均値として推定される。  - `estimatedGateDischargeCoefficient`: 水門の校正された排出係数。  - `id`: エンティティのユニークな識別子  - `initialConditions`: シミュレーションのためにRegulation Structureに適用される修正のセットの説明。  - `inputParameters`: シミュレーションのためにRegulation Structureに適用される修正のセットの説明。  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `modelError`: 観測された放電量とシミュレーションされた放電量の誤差の割合。  - `modelledDischarge`: シミュレーションモデルから推定される排出量。  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `simulationOutput`: 規制構造のシミュレーション結果一式の説明。  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `spillwayFlow`: 新しい総排水量に対する放水路排水量の割合  - `startSimulationTime`: シミュレーションを開始する時刻（ISO8601 UTC形式）。  - `targetDischarge`: 公益事業者が定めた、水路に設置される望ましい排出量。  - `type`: NGSI-LD エンティティタイプ。RegulationStructureSimulationである必要があります。    
必須項目  
- `id`  - `type`  ## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RegulationStructureSimulation:    
  description: 'This entity contains a harmonised description of a data model for regulation structure simulation, for Raw-Water (Open Channels) System Management domain.'    
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
    endSimulationTime:    
      description: 'Time of day in ISO8601 UTC format at which the simulation ends.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    equivalentSluiceOpening:    
      description: 'Equivalent sluice gate opening in the case of multiple sluice gates, estimated as the mean value of the different openings.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    estimatedGateDischargeCoefficient:    
      description: 'Calibrated discharge coefficient of the sluice gate.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &regulationstructuresimulation_-_properties_-_owner_-_items_-_anyof    
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
    initialConditions:    
      description: 'Description of the set of the modifications to be applied to the Regulation Structure for the simulation.'    
      items:    
        properties:    
          targetURI:    
            anyOf:    
              - description: 'Property. Identifier format of any NGSI entity'    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              - description: 'Property. Identifier format of any NGSI entity'    
                format: uri    
                type: string    
            description: 'Relationship. A relationship indicating the network component with a simulated property value.'    
          value:    
            anyOf:    
              - type: string    
              - type: number    
              - type: boolean    
          waterAttribute:    
            description: 'Property: An attribute issued from the data models for Open Channel Management. It follows fully this data model and it could be a property or a relationship. It contains the values for specified properties, as derive from the simulation.'    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    inputParameters:    
      description: 'Description of the set of the modifications to be applied to the Regulation Structure for the simulation.'    
      items:    
        properties:    
          targetURI:    
            anyOf:    
              - description: 'Property. Identifier format of any NGSI entity'    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              - description: 'Property. Identifier format of any NGSI entity'    
                format: uri    
                type: string    
            description: 'Relationship. A relationship indicating the network component with a simulated property value.'    
          value:    
            anyOf:    
              - type: string    
              - type: number    
              - type: boolean    
          waterAttribute:    
            description: 'Property: An attribute issued from the data models for Open Channel Management. It follows fully this data model and it could be a property or a relationship. It contains the values for specified properties, as derive from the simulation.'    
            type: string    
        type: object    
      type: array    
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
    modelError:    
      description: 'Percentage error between observed and simulated discharge.'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    modelledDischarge:    
      description: 'Discharge estimated from the simulation model.'    
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
        anyOf: *regulationstructuresimulation_-_properties_-_owner_-_items_-_anyof    
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
    simulationOutput:    
      description: 'Description of the set of results of simulation of the regulation structure.'    
      items:    
        properties:    
          targetURI:    
            anyOf:    
              - description: 'Property. Identifier format of any NGSI entity'    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              - description: 'Property. Identifier format of any NGSI entity'    
                format: uri    
                type: string    
            description: 'Relationship. A relationship indicating the network component with a simulated property value.'    
          value:    
            anyOf:    
              - type: string    
              - type: number    
              - type: boolean    
          waterAttribute:    
            description: 'Property: An attribute issued from the data models for Open Channel Management. It follows fully this data model and it could be a property or a relationship. It contains the values for specified properties, as derive from the simulation.'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    spillwayFlow:    
      description: 'Ratio of the spillway discharge to the new total discharge'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    startSimulationTime:    
      description: 'Time of day in ISO8601 UTC format at which the simulation begins.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    targetDischarge:    
      description: 'Desirable discharge to be established in the channel, defined by the utility’s operators.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It has to be RegulationStructureSimulation.'    
      enum:    
        - RegulationStructureSimulation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### RegulationStructureSimulation NGSI-v2 key-values例  
ここでは、JSON-LD形式でkey-valuesとしてRegulationStructureSimulationの例を示します。これは`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### RegulationStructureSimulation NGSI-v2の正規化例  
ここでは、正規化されたJSON-LD形式のRegulationStructureSimulationの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### RegulationStructureSimulation NGSI-LD key-values Example  
RegulationStructureSimulationをkey-valuesとしてJSON-LD形式で表現した例を示します。これは、`options=keyValues`を使用した場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### RegulationStructureSimulation NGSI-LDの正規化例  
ここでは、正規化されたJSON-LD形式のRegulationStructureSimulationの例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:RegulationStructureSimulation:id:SCAU:96103454",  
  "type": "RegulationStructureSimulation",  
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
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "Regulation_Structure_Simulation_1"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Regulation Structure Simulation 1"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Regulation Structure Simulation"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "NTUA"  
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
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -27.391838,  
        -16.801411  
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
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": ""  
  },  
  "startSimulationTime": {  
    "type": "Property",  
    "value": {  
      "@type": "Datetime",  
      "@value": "2020-12-19T09:55:49Z"  
    }  
  },  
  "endSimulationTime": {  
    "type": "Property",  
    "value": {  
      "@type": "Datetime",  
      "@value": "2020-12-19T09:56:49Z"  
    }  
  },  
  "modelError": {  
    "type": "Property",  
    "value": 0.004  
  },  
  "targetDischarge": {  
    "type": "Property",  
    "value": 14  
  },  
  "modelledDischarge": {  
    "type": "Property",  
    "value": 14  
  },  
  "spillwayFlow": {  
    "type": "Property",  
    "value": 0  
  },  
  "estimatedGateDischargeCoefficient": {  
    "type": "Property",  
    "value": 0.401  
  },  
  "equivalentSluiceOpening": {  
    "type": "Property",  
    "value": 490  
  },  
  "simulationOutput": {  
    "type": "Property",  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
