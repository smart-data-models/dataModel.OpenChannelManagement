<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。横断面  
======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/CrossSection/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**该实体包含对原水（明渠）系统管理领域的通用横截面的统一描述。横断面定义了系统中由设备监测原水属性和/或通过模拟计算的任何点。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `attachedTo[*]`: 与横断面 "居住 "的通道ID的关系。对通道类型的实体的引用。  - `bottomSlope[number]`: 横断面 "居住 "的渠道的底部坡度。所有单位都接受CEFACT代码。  - `bottomWidth[number]`: 横截面的底部宽度（对于 "梯形 "几何形状）。所有单位都接受CEFACT代码。  - `crossSectionGeometry[string]`: 横断面的几何形状。Enum:'Circular, Trapezoidal'.  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `diameter[number]`: 一个圆形截面的直径。  - `energyHead[number]`: 横断面的总能量头。  - `id[*]`: 实体的唯一标识符  - `inheritsFrom[*]`: 一个通道组件的URI，从该组件中获得一个属性的值。  - `leftSideSlope[number]`: 横断面左岸的坡度（用于 "梯形 "几何形状）。所有单位都接受CEFACT代码。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `maxWaterDepth[number]`: 横断面上的最大允许水深。所有单位都接受CEFACT代码。  - `name[string]`: 这个项目的名称。  - `observedBy[*]`: 与监测原水特性的设备的ID的关系  . Model: [https://smart-data-models.github.io/dataModel.Device/device-schema.json](https://smart-data-models.github.io/dataModel.Device/device-schema.json)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `position[object]`: 提供与其他元素的距离信息和与它们的关系的对象。  - `rightSideSlope[number]`: 横断面右岸的坡度（用于 "梯形 "几何形状）。所有单位都接受CEFACT代码。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `specificConductivity[number]`: 横断面的导水率。  - `tag[string]`: 一个可选的文本字符串，用于限定一个项目  . Model: [https://schema.org/Text](https://schema.org/Text)- `turbidity[number]`: 横断面的水浊度。  - `type[string]`: NGSI-LD实体类型。它必须是CrossSection。  - `waterFlow[number]`: 横断面上的水流。  - `waterLevel[number]`: 横断面的水位。  - `waterTemperature[number]`: 横断面的水温。  - `waterVelocity[number]`: 横断面的水速。  <!-- /30-PropertiesList -->  
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
CrossSection:    
  description: 'This entity contains a harmonised description of a generic Cross-Section made for Raw-Water (Open Channels) System Management domain. A CrossSection defines any point of the system where raw-water properties are monitored by a device and/or computed via simulation.'    
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
    attachedTo:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship to the ID of the channel where the cross-section ''lives in''. Reference to an entity of type Channel.'    
      x-ngsi:    
        type: Relationship    
    bottomSlope:    
      description: 'The bottom slope of the channel where the cross-section ''lives in''. All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    bottomWidth:    
      description: 'The bottom width of the cross-section (for ''Trapezoidal'' geometry). All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    crossSectionGeometry:    
      description: 'The geometry of the cross-section. Enum:''Circular, Trapezoidal''.'    
      enum:    
        - Circular    
        - Trapezoidal    
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
    diameter:    
      description: 'The diameter of a circular cross-section.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    energyHead:    
      description: 'The total energy head at the cross-section.'    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &crosssection_-_properties_-_owner_-_items_-_anyof    
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
    inheritsFrom:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'URI of a Channel component from which the value of a property is obtained.'    
      x-ngsi:    
        type: Relationship    
    leftSideSlope:    
      description: 'The slope of the left bank of the cross-section (for ''Trapezoidal'' geometry). All units are accepted in CEFACT code.'    
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
      description: 'The maximum allowable water depth at the cross-section. All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
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
        anyOf: *crosssection_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    position:    
      description: 'Object providing information about the distance with the rest of the elements and a relationship with them.'    
      properties:    
        distance:    
          description: 'Property. The distance between this Entity and a reference point (e.g., the most upstream point of the system).'    
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
    rightSideSlope:    
      description: 'The slope of the right bank of the cross-section (for ''Trapezoidal'' geometry). All units are accepted in CEFACT code.'    
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
    specificConductivity:    
      description: 'Water conductivity at the cross-section.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    tag:    
      description: 'An optional text string used to qualify an item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    turbidity:    
      description: 'Water turbidity at the cross-section.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It has to be CrossSection.'    
      enum:    
        - CrossSection    
      type: string    
      x-ngsi:    
        type: Property    
    waterFlow:    
      description: 'Water flow at the cross-section.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    waterLevel:    
      description: 'Water level at the cross-section.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    waterTemperature:    
      description: 'Water temperature at the cross-section.'    
      type: number    
      x-ngsi:    
        type: Property    
    waterVelocity:    
      description: 'Water Velocity at the cross-section.'    
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
## ＃＃＃＃有效载荷的例子  
#### CrossSection NGSI-v2 key-values 示例  
这里有一个以JSON-LD格式作为key-values的CrossSection的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### 横断面NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的CrossSection的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:CrossSection:items:ILNP:15826171",  
      "urn:ngsi-ld:CrossSection:items:RUEP:96519173"  
    ]  
  },  
  "seeAlso": {  
    "type": "Array",  
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
    "type": "StructuredObject",  
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
    "type": "object",  
    "value": "urn:ngsi-ld:CrossSection:attachedTo:CTHP:74683243"  
  },  
  "observedBy": {  
    "type": "object",  
    "value": "urn:ngsi-ld:CrossSection:observedBy:WJTI:74120377"  
  },  
  "tag": {  
    "type": "Text",  
    "value": ""  
  },  
  "position": {  
    "type": "StructuredObject",  
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
    "type": "Number",  
    "value": 0  
  },  
  "maxWaterDepth": {  
    "type": "Number",  
    "value": 4  
  },  
  "inheritsFrom": {  
    "type": "object",  
    "value": "urn:ngsi-ld:CrossSection:inheritsFrom:JXFD:60487647"  
  }  
}  
```  
</details>  
#### 横断面NGSI-LD关键值示例  
这里是一个以JSON-LD格式作为key-values的CrossSection的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### 横断面NGSI-LD正常化的例子  
下面是一个以JSON-LD格式规范化的CrossSection的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
        "type": "Geoproperty",  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
