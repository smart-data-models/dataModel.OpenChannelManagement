<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。监管结构  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/RegulationStructure/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**该实体包含对原水（明渠）系统管理领域的通用调节结构的统一描述。调节结构代表了一个结点类型的对象，控制原水系统中的水流量。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `hasSluiceGate[*]`: 对一个水闸类型的实体的引用。  - `hasSpillway[*]`: 对Sluice gate Spillway类型实体的引用。  - `id[*]`: 实体的唯一标识符  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `numberOfGates[number]`: 一个整数值，定义连接到调节结构的控制门的数量。  - `numberOfSpillways[number]`: 一个整数值，定义连接到调节结构的溢流道的数量。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `position[object]`: 提供与其他元素的距离信息和与它们的关系的对象。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `tag[string]`: 一个可选的文本字符串，用于限定一个项目  . Model: [https://schema.org/Text](https://schema.org/Text)- `teleCommand[boolean]`: 定义调节结构是远程控制还是手动控制。真/假值。  - `type[string]`: NGSI-LD实体类型。它必须是RegulationStructure  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RegulationStructure:    
  description: 'This entity contains a harmonised description of a generic Regulation Structure made for Raw-Water (Open Channels) System Management domain. Regulation structure represents a junction-type object, controlling the water flow in the raw-water system.'    
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
    hasSluiceGate:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to an entity of type Sluice gate.'    
      x-ngsi:    
        type: Relationship    
    hasSpillway:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to an entity of type Sluice gate Spillway.'    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: &regulationstructure_-_properties_-_owner_-_items_-_anyof    
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
    numberOfGates:    
      description: 'An integer value defining the number of control gates attached to the regulation structure.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfSpillways:    
      description: 'An integer value defining the number of spillways attached to the regulation structure.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *regulationstructure_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    position:    
      description: 'Object providing information about the distance with the rest of the elements and a relationship with them.'    
      properties:    
        distance:    
          description: 'Property. The distance between this Entity and a reference point (e.g., the most upstream point of the system). Units:''Km'' '    
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
    teleCommand:    
      description: 'Define whether the regulation structure is controlled remotely or manually. True/False value.'    
      type: boolean    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It has to be RegulationStructure'    
      enum:    
        - RegulationStructure    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/RegulationStructure/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/RegulationStructure/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### RegulationStructure NGSI-v2 key-values 示例  
下面是一个以JSON-LD格式作为key-values的RegulationStructure的例子。当使用`options=keyValues'时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RegulationStructure:id:IXHN:40075061",  
  "type": "RegulationStructure",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -72.3447045,  
      44.679442  
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
  "dateCreated": "1986-07-26T02:43:28Z",  
  "dateModified": "2021-03-21T17:56:26Z",  
  "source": "",  
  "name": "RS01",  
  "alternateName": "RS01 Thivae",  
  "description": "Regulation Structure Thivae",  
  "dataProvider": "EYDAP",  
  "owner": [  
    "urn:ngsi-ld:RegulationStructure:items:ASWJ:21246595",  
    "urn:ngsi-ld:RegulationStructure:items:NHFZ:56673870"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RegulationStructure:items:PLEL:78574823",  
    "urn:ngsi-ld:RegulationStructure:items:IZVF:62633698"  
  ],  
  "tag": "",  
  "numberOfGates": 1,  
  "numberOfSpillways": 1,  
  "teleCommand": true,  
  "hasSluiceGate": "urn:ngsi-ld:RegulationStructure:hasSluiceGate:JXFD:60487647",  
  "hasSpillway": "urn:ngsi-ld:RegulationStructure:hasSpillway:CBWI:21948924",  
  "position": {  
    "distance": 160.6,  
    "refPoint": "urn:ngsi-ld:RegulationStructure:refPoint:JXFD:60487647"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### RegulationStructure NGSI-v2 normalized Example  
下面是一个规范化的JSON-LD格式的RegulationStructure的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RegulationStructure:id:IXHN:40075061",  
  "type": "RegulationStructure",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -72.3447045,  
        44.679442  
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
    "value": "1986-07-26T02:43:28Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2021-03-21T17:56:26Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "RS01"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "RS01 Thivae"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Regulation Structure Thivae"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:RegulationStructure:items:ASWJ:21246595",  
      "urn:ngsi-ld:RegulationStructure:items:NHFZ:56673870"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:RegulationStructure:items:PLEL:78574823",  
      "urn:ngsi-ld:RegulationStructure:items:IZVF:62633698"  
    ]  
  },  
  "tag": {  
    "type": "Text",  
    "value": ""  
  },  
  "numberOfGates": {  
    "type": "Number",  
    "value": 1  
  },  
  "numberOfSpillways": {  
    "type": "Number",  
    "value": 1  
  },  
  "teleCommand": {  
    "type": "Boolean",  
    "value": "true"  
  },  
  "hasSluiceGate": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:RegulationStructure:hasSluiceGate:JXFD:60487647"  
  },  
  "hasSpillway": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:RegulationStructure:hasSpillway:CBWI:21948924"  
  },  
  "position": {  
    "type": "StructuredValue",  
    "value": {  
      "distance": 160.6,  
      "refPoint": "urn:ngsi-ld:RegulationStructure:refPoint:JXFD:60487647"  
    }  
  }  
}  
```  
</details>  
#### RegulationStructure NGSI-LD key-values 示例  
下面是一个以JSON-LD格式作为key-values的RegulationStructure的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RegulationStructure:id:IXHN:40075061",  
    "type": "RegulationStructure",  
    "address": {  
        "streetAddress": "",  
        "addressLocality": "",  
        "addressRegion": "",  
        "addressCountry": "",  
        "postalCode": "",  
        "postOfficeBoxNumber": "",  
        "areaServed": ""  
    },  
    "alternateName": "RS01 Thivae",  
    "areaServed": "",  
    "dataProvider": "EYDAP",  
    "dateCreated": "1986-07-26T02:43:28Z",  
    "dateModified": "2021-03-21T17:56:26Z",  
    "description": "Regulation Structure Thivae",  
    "hasSluiceGate": "urn:ngsi-ld:RegulationStructure:hasSluiceGate:JXFD:60487647",  
    "hasSpillway": "urn:ngsi-ld:RegulationStructure:hasSpillway:CBWI:21948924",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -72.3447045,  
            44.679442  
        ]  
    },  
    "name": "RS01",  
    "numberOfGates": 1,  
    "numberOfSpillways": 1,  
    "owner": [  
        "urn:ngsi-ld:RegulationStructure:items:ASWJ:21246595",  
        "urn:ngsi-ld:RegulationStructure:items:NHFZ:56673870"  
    ],  
    "position": {  
        "distance": 160.6,  
        "refPoint": "urn:ngsi-ld:RegulationStructure:refPoint:JXFD:60487647"  
    },  
    "seeAlso": [  
        "urn:ngsi-ld:RegulationStructure:items:PLEL:78574823",  
        "urn:ngsi-ld:RegulationStructure:items:IZVF:62633698"  
    ],  
    "source": "",  
    "tag": "",  
    "teleCommand": true,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### RegulationStructure NGSI-LD normalized Example  
下面是一个规范化的JSON-LD格式的RegulationStructure的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RegulationStructure:id:IXHN:40075061",  
    "type": "RegulationStructure",  
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
        "value": "RS01 Thivae"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "EYDAP"  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1986-07-26T02:43:28Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-03-21T17:56:26Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Regulation Structure Thivae"  
    },  
    "hasSluiceGate": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:RegulationStructure:hasSluiceGate:JXFD:60487647"  
    },  
    "hasSpillway": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:RegulationStructure:hasSpillway:CBWI:21948924"  
    },  
    "location": {  
        "type": "Geoproperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -72.3447045,  
                44.679442  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "RS01"  
    },  
    "numberOfGates": {  
        "type": "Property",  
        "value": 1  
    },  
    "numberOfSpillways": {  
        "type": "Property",  
        "value": 1  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:RegulationStructure:items:ASWJ:21246595",  
            "urn:ngsi-ld:RegulationStructure:items:NHFZ:56673870"  
        ]  
    },  
    "position": {  
        "type": "Property",  
        "value": {  
            "distance": 160.6,  
            "refPoint": "urn:ngsi-ld:RegulationStructure:refPoint:JXFD:60487647"  
        }  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:RegulationStructure:items:PLEL:78574823",  
            "urn:ngsi-ld:RegulationStructure:items:IZVF:62633698"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "tag": {  
        "type": "Property",  
        "value": ""  
    },  
    "teleCommand": {  
        "type": "Property",  
        "value": true  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
