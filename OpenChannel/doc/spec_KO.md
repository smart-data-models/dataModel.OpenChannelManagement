<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 엔티티: OpenChannel  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/OpenChannel/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **이 엔티티에는 원수(개방형 채널) 시스템 관리 도메인용으로 만들어진 일반 채널에 대한 조화로운 설명이 포함되어 있습니다.**  
버전: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `bottomSlope[number]`: 채널의 하단 경사도입니다. 모든 단위는 CEFACT 코드로 허용됩니다.  - `bottomWidth[number]`: 채널의 하단 너비('사다리꼴' 지오메트리의 경우). 모든 단위는 CEFACT 코드에서 허용됩니다.  - `celerity[number]`: 수문 개방 또는 폐쇄 후 채널을 따라 전파되는 서지의 속도  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `diameter[number]`: 원형 채널의 지름입니다. 모든 단위는 CEFACT 코드로 허용됩니다.  - `downstreamNode[*]`: 채널이 끝나는 다운스트림 노드(예: 정션, 레귤레이션 구조)의 ID를 나타내는 관계입니다.  - `flowType[string]`: 채널의 흐름 유형을 정의하는 텍스트입니다. Enum:'자유 표면 흐름'  - `geometryType[string]`: 채널의 지오메트리입니다. Enum:'사다리꼴, 원형']  - `id[*]`: 엔티티의 고유 식별자  - `leftSideSlope[number]`: 채널 왼쪽 뱅크의 기울기('사다리꼴' 지오메트리의 경우). 모든 단위는 CEFACT 코드로 허용됩니다.  - `length[number]`: 채널의 길이입니다. 모든 단위는 CEFACT 코드로 허용됩니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `maxWaterDepth[number]`: 채널에서 허용되는 최대 수심입니다. 모든 단위는 CEFACT 코드에서 허용됩니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `rightSideSlope[number]`: 채널 오른쪽 뱅크의 경사('사다리꼴' 지오메트리의 경우)입니다. 모든 단위는 CEFACT 코드에서 허용됩니다.  - `roughnessCoefficient[number]`: 매닝의 거칠기 계수  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `tag[string]`: 항목을 한정하는 데 사용되는 선택적 텍스트 문자열입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `travelDuration[number]`: 다운스트림 노드(즉, 레귤레이션 구조)에서 업스트림 노드로 이동하는 서지 기간입니다.  - `type[string]`: NGSI-LD 엔티티 유형. OpenChannel이어야 합니다.  - `upstreamNode[*]`: 채널이 시작되는 업스트림 노드(예: 정션, 레귤레이션 구조)의 ID를 나타내는 관계입니다.  - `waterLoss[number]`: 채널의 누수/손실 - 채널의 유량 백분율 또는 숫자(유량)  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OpenChannel:    
  description: This entity contains a harmonised description of a generic Channel made for Raw-Water (Open Channels) System Management domain.    
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
    bottomSlope:    
      description: The bottom slope of the channel. All units are accepted in CEFACT code    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    bottomWidth:    
      description: The bottom width of the channel (for 'Trapezoidal' geometry). All units are accepted in CEFACT code    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    celerity:    
      description: Velocity of a surge propagated along the channel after the opening or close of a sluice gate    
      minimum: 0    
      type: number    
      x-ngsi:    
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
    diameter:    
      description: The diameter of a circular channel. All units are accepted in CEFACT code    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    downstreamNode:    
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
      description: 'A relationship indicating the ID of the downstream node (e.g., Junction, Regulation Structure), where the channel ends'    
      x-ngsi:    
        type: Relationship    
    flowType:    
      description: 'Text defining the type of flow in the channel. Enum:''Free-Surface flow'''    
      enum:    
        - Free-Surface flow    
      type: string    
      x-ngsi:    
        type: Property    
    geometryType:    
      description: 'The geometry of the channel. Enum:''Trapezoidal, Circular'']'    
      enum:    
        - Circular    
        - Trapezoidal    
      type: string    
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
    leftSideSlope:    
      description: The slope of the left bank of the channel (for 'Trapezoidal' geometry). All units are accepted in CEFACT code    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    length:    
      description: The length of the channel. All units are accepted in CEFACT code    
      minimum: 0    
      type: number    
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
    maxWaterDepth:    
      description: The maximum allowable water depth in the channel. All units are accepted in CEFACT code    
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
    rightSideSlope:    
      description: The slope of the right bank of the channel (for 'Trapezoidal' geometry). All units are accepted in CEFACT code    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    roughnessCoefficient:    
      description: The Manning’s roughness coefficient    
      minimum: 0    
      type: number    
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
    tag:    
      description: An optional text string used to qualify an item    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    travelDuration:    
      description: 'The duration of the surge travelling from the downstream node (i.e., Regulation Structure) to the upstream node'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI-LD Entity Type. it has to be OpenChannel    
      enum:    
        - OpenChannel    
      type: string    
      x-ngsi:    
        type: Property    
    upstreamNode:    
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
      description: 'A relationship indicating the ID of the upstream node (e.g., Junction, Regulation Structure), where the channel begins'    
      x-ngsi:    
        type: Relationship    
    waterLoss:    
      description: Water leakages/losses from the channel - percentage of flow of the channel or a number (flow)    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
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
## 페이로드 예시  
#### OpenChannel NGSI-v2 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 OpenChannel의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### OpenChannel NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 OpenChannel의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### OpenChannel NGSI-LD 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 OpenChannel의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### OpenChannel NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 OpenChannel 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
