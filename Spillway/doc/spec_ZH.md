<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
单位：Spillway泄洪道  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/Spillway/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**本实体包含对原水（明渠）系统管理域通用泄洪道的统一描述。泄洪道代表一个枢纽型对象，控制下游水坝或调节结构的泄洪**。  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: 该项目的替代名称  - `apronElevation[number]`: 溢洪道上游弧形溢洪道结构 (P) 底部的标高  - `apronLength[number]`: 泄洪道底部总长度  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `controlCrossSection[*]`: 表示断面类型实体 ID 的关系，表示控制溢洪道水流的断面  - `crestElevation[number]`: 泄洪道的坡顶标高。仅 "宽顶"、"椭圆形 "和 "尖顶 "需要填写。  - `crestLength[number]`: 泄洪道的长度等于水流通过的总长度。仅对 "宽顶"、"椭圆形 "和 "尖顶 "有要求。  - `curveDesignDischargeCoefficient[*]`: OpenChannelCurve 实体的 URI，表示设计排泄系数 (Co) 与设计上游水头上停机坪标高的函数关系 (Co-P/Ho)  - `curveDischargeCoefficient[*]`: OpenChannelCurve 实体的 URI，表示排泄系数 (C) 与上游水头 (H) 和溢洪道几何形状的函数关系。例如，作为上游水头与溢洪道宽度（C-H/L）函数的泄洪系数，或 C/Co-H/Ho  - `curveElevationDischarge[*]`: OpenChannelCurve 实体的 URI，该实体表示作为水位高程 (H) 函数的排水量 (Q)  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `designDischarge[number]`: 泄洪道的设计排水量 (Qo)  - `designDischargeCoefficient[number]`: 设计排量 (Ho) 的能量损失排量系数 (Co)  - `designHead[number]`: 为 "弧形溢洪道 "设计的上游总水头 (Ho)  - `dischargeCoefficient[number]`: 水流进入、流动和流出溢洪道时能量损失的排泄系数  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `maxFloodElevation[number]`: 可通过泄洪道的最大水位高程  - `name[string]`: 该项目的名称  - `numberAbutments[number]`: 椭圆形溢洪道的墩台数量。仅适用于 "Ogee "类型  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `spillwayType[string]`: 泄洪道类型。如果是 "指定泄洪道"，则只需要 "高程-泄量 "曲线。枚举：'宽顶、椭圆形、尖顶、指定泄洪道'。  - `spillwayWidth[number]`: 泄洪道宽度（米）。仅适用于 "宽顶 "型  - `tag[string]`: 用于限定项目的可选文本字符串  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI 实体类型。必须是溢洪道  - `waterDischarge[number]`: 溢洪道上的排水量 (Q)  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `location`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Spillway:    
  description: 'This entity contains a harmonised description for a generic Spillway made for Raw-Water (Open Channels) System Management domain. Spillway represents a junction-type object, controlling the release of water from a dam or regulation structure downstream.'    
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
    apronElevation:    
      description: 'The elevation at the bottom of the ogee spillway structure (P), just upstream of the spillway'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    apronLength:    
      description: The total length of the spillway bottom    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    controlCrossSection:    
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
      description: 'A relationship indicating the ID of an entity of type Cross Section, indicating the cross section that controls the flow over the Spillway'    
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
      description: The URI of an OpenChannelCurve entity that represents the design discharge coefficient (Co) as a function of apron Elevation over design upstream head (Co-P/Ho)    
      x-ngsi:    
        type: Relationship    
    curveDischargeCoefficient:    
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
      description: 'The URI of an OpenChannelCurve entity that represents the discharge coefficient (C) as a function of upstream head (H) and spillway geometry. For instance, discharge coefficient as a function of upstream head over spillway width (C-H/L), or C/Co-H/Ho'    
      x-ngsi:    
        type: Relationship    
    curveElevationDischarge:    
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
      description: The URI of an OpenChannelCurve entity that represents discharge (Q) as a function of water elevation (H)    
      x-ngsi:    
        type: Relationship    
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
    designDischarge:    
      description: The design discharge (Qo) of the Spillway    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: ' m^3/s'    
    designDischargeCoefficient:    
      description: The discharge coefficient (Co) for energy losses for the design discharge (Ho)    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    designHead:    
      description: The total upstream energy head for which the spillway is designed (Ho) for 'Ogee Spillway'    
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
        units: m^0.5/s    
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
    maxFloodElevation:    
      description: The maximum elevation of water that can pass the spillway    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    numberAbutments:    
      description: The number of abutments of an ogee spillway. Only for 'Ogee' type    
      minimum: 0    
      type: number    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    spillwayType:    
      description: 'The type of the spillway. In the case of “Specified Spillway”, only “Elevation – discharge” curve is required. Enum:''Broad-Crested, Ogee, Sharp-Crested, Specified Spillway'''    
      enum:    
        - Broad-Crested    
        - Ogee    
        - Sharp-Crested    
        - Specified Spillway    
      type: string    
      x-ngsi:    
        type: Property    
    spillwayWidth:    
      description: The width of the spillway (m). Only for 'Broad-Crested' type    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    tag:    
      description: An optional text string used to qualify an item    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity Type. It has to be Spillway    
      enum:    
        - Spillway    
      type: string    
      x-ngsi:    
        type: Property    
    waterDischarge:    
      description: The discharge over the spillway (Q)    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
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
## 有效载荷示例  
#### Spillway NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 Spillway 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### Spillway NGSI-v2 归一化示例  
下面是一个规范化 JSON-LD 格式的溢洪道示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### 泄洪道 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 Spillway 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
#### 溢洪道 NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的溢洪道示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
        "type": "GeoProperty",  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
