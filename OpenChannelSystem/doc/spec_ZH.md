<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。开放通道系统  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/OpenChannelSystem/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**该实体包含对原水（明渠）系统管理领域的通用系统的统一描述。该实体代表由不同组件（如渠道、连接点、断面等）组成的系统，或仅代表一个组件（如水闸）**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `hasSubSystem[*]`: 对OpenChannelSystem类型实体的引用--一个开放通道子系统。  - `id[*]`: 实体的唯一标识符  - `isComposedOf[*]`: 指明渠系统的组成实体，类型为渠道、横断面、交界处、调节结构、水闸、泄洪道。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `mostDownstreamPoint[*]`: 表示系统最下游节点（如结点或横断面）的ID的关系。  - `mostUpstreamPoint[*]`: 表示系统最上游节点（例如，一个结点或一个横断面）的ID的关系。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: NGSI-LD实体类型。它必须是OpenChannelSystem  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OpenChannelSystem:    
  description: 'This entity contains a harmonised description of a generic system made for Raw-Water (Open Channels) System Management domain. This entity represents either a system composed of different components (e.g., channels, junctions, cross-sections etc.) or just a component (e.g., a SluiceGate).'    
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
    hasSubSystem:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to an entity of type OpenChannelSystem - an open-channel sub-system.'    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: &openchannelsystem_-_properties_-_owner_-_items_-_anyof    
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
    isComposedOf:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the component entities of the open-channel system, of type Channel, Cross-Section, Junction, Regulation Structure, SluiceGate, Spillway.'    
      x-ngsi:    
        type: Relationship    
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
    mostDownstreamPoint:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of the most downstream node (e.g., a Junction or a Cross-section) of the system.'    
      x-ngsi:    
        type: Relationship    
    mostUpstreamPoint:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of the most upstream node (e.g., a Junction or a Cross-section) of the system.'    
      x-ngsi:    
        type: Relationship    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *openchannelsystem_-_properties_-_owner_-_items_-_anyof    
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
    type:    
      description: 'NGSI-LD Entity Type. It has to be OpenChannelSystem'    
      enum:    
        - OpenChannelSystem    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/OpenChannelSystem/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/OpenChannelSystem/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### OpenChannelSystem NGSI-v2 关键值示例  
下面是一个以JSON-LD格式作为关键值的OpenChannelSystem的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelSystem:id:EHTH:11109231",  
  "type": "OpenChannelSystem",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      59.820118,  
      -157.397178  
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
  "dateCreated": "2020-12-07T21:37:19Z",  
  "dateModified": "2021-07-14T01:06:03Z",  
  "source": "",  
  "name": "L7 - L11",  
  "alternateName": "",  
  "description": "Conveyance System near Thivae",  
  "dataProvider": "EYDAP",  
  "owner": [  
    "urn:ngsi-ld:OpenChannelSystem:items:WPHN:07387656",  
    "urn:ngsi-ld:OpenChannelSystem:items:JNVF:94407376"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:OpenChannelSystem:items:EZUE:70603867",  
    "urn:ngsi-ld:OpenChannelSystem:items:MWLT:38533440"  
  ],  
  "isComposedOf": "urn:ngsi-ld:OpenChannelSystem:isComposedOf:UMLF:11032914",  
  "hasSubSystem": "urn:ngsi-ld:OpenChannelSystem:hasSubSystem:BYUP:86302765",  
  "mostUpstreamPoint": "urn:ngsi-ld:OpenChannelSystem:mostUpstreamPoint:YUHY:75075828",  
  "mostDownstreamPoint": "urn:ngsi-ld:OpenChannelSystem:mostDownstreamPoint:IXHM:68215414"  
}  
```  
</details>  
#### OpenChannelSystem NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的OpenChannelSystem的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelSystem:id:EHTH:11109231",  
  "type": "OpenChannelSystem",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        59.820118,  
        -157.397178  
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
    "value": "2020-12-07T21:37:19Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2021-07-14T01:06:03Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "L7 - L11"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "Conveyance System near Thivae"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:OpenChannelSystem:items:WPHN:07387656",  
      "urn:ngsi-ld:OpenChannelSystem:items:JNVF:94407376"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:OpenChannelSystem:items:EZUE:70603867",  
      "urn:ngsi-ld:OpenChannelSystem:items:MWLT:38533440"  
    ]  
  },  
  "isComposedOf": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:OpenChannelSystem:isComposedOf:UMLF:11032914"  
  },  
  "hasSubSystem": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:OpenChannelSystem:hasSubSystem:BYUP:86302765"  
  },  
  "mostUpstreamPoint": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:OpenChannelSystem:mostUpstreamPoint:YUHY:75075828"  
  },  
  "mostDownstreamPoint": {  
    "type": "object",  
    "value": "urn:ngsi-ld:OpenChannelSystem:mostDownstreamPoint:IXHM:68215414"  
  }  
}  
```  
</details>  
#### OpenChannelSystem NGSI-LD关键值示例  
下面是一个以JSON-LD格式作为关键值的OpenChannelSystem的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:OpenChannelSystem:id:EHTH:11109231",  
    "type": "OpenChannelSystem",  
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
    "dataProvider": "EYDAP",  
    "dateCreated": "2020-12-07T21:37:19Z",  
    "dateModified": "2021-07-14T01:06:03Z",  
    "description": "Conveyance System near Thivae",  
    "hasSubSystem": "urn:ngsi-ld:OpenChannelSystem:hasSubSystem:BYUP:86302765",  
    "isComposedOf": "urn:ngsi-ld:OpenChannelSystem:isComposedOf:UMLF:11032914",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            59.820118,  
            -157.397178  
        ]  
    },  
    "mostDownstreamPoint": "urn:ngsi-ld:OpenChannelSystem:mostDownstreamPoint:IXHM:68215414",  
    "mostUpstreamPoint": "urn:ngsi-ld:OpenChannelSystem:mostUpstreamPoint:YUHY:75075828",  
    "name": "L7 - L11",  
    "owner": [  
        "urn:ngsi-ld:OpenChannelSystem:items:WPHN:07387656",  
        "urn:ngsi-ld:OpenChannelSystem:items:JNVF:94407376"  
    ],  
    "seeAlso": [  
        "urn:ngsi-ld:OpenChannelSystem:items:EZUE:70603867",  
        "urn:ngsi-ld:OpenChannelSystem:items:MWLT:38533440"  
    ],  
    "source": "",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### OpenChannelSystem NGSI-LD规范化示例  
下面是一个以JSON-LD格式规范化的OpenChannelSystem的例子。在不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:OpenChannelSystem:id:EHTH:11109231",  
    "type": "OpenChannelSystem",  
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
    "dataProvider": {  
        "type": "Property",  
        "value": "EYDAP"  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-12-07T21:37:19Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-07-14T01:06:03Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Conveyance System near Thivae"  
    },  
    "hasSubSystem": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:OpenChannelSystem:hasSubSystem:BYUP:86302765"  
    },  
    "isComposedOf": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:OpenChannelSystem:isComposedOf:UMLF:11032914"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                59.820118,  
                -157.397178  
            ]  
        }  
    },  
    "mostDownstreamPoint": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:OpenChannelSystem:mostDownstreamPoint:IXHM:68215414"  
    },  
    "mostUpstreamPoint": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:OpenChannelSystem:mostUpstreamPoint:YUHY:75075828"  
    },  
    "name": {  
        "type": "Property",  
        "value": "L7 - L11"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:OpenChannelSystem:items:WPHN:07387656",  
            "urn:ngsi-ld:OpenChannelSystem:items:JNVF:94407376"  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:OpenChannelSystem:items:EZUE:70603867",  
            "urn:ngsi-ld:OpenChannelSystem:items:MWLT:38533440"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
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
