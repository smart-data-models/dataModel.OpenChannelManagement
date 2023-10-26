<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

========================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  
	- `refPoint[*]`: 기준점 거리는 다음에서 측정됩니다.    
- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

OpenChannelJunction:    
  description: 'This entity contains a harmonised description of a generic Junction made for Raw-Water (Open Channels) System Management domain. A Junction defines a location where the characteristics of the channel changes, two or more channels come together or split apart, amounts of water are abstracted or inserted to the system etc.'    
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
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    observedBy:    
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
      description: A relationship to the ID of the device that monitors raw-water properties    
      x-ngsi:    
        model: https://smart-data-models.github.io/dataModel.Device/device-schema.json    
        type: Relationship    
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
    position:    
      description: Object providing information about the distance with the rest of the elements and a relationship with them    
      properties:    
        distance:    
          description: 'The distance between this Entity and a reference point (e.g., the most upstream point of the system)'    
          type: number    
          x-ngsi:    
            type: Property    
            units: ' Km'    
        refPoint:    
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
          description: The reference point distance is measured from    
          x-ngsi:    
            type: Relationship    
      type: object    
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
    type:    
      description: NGSI Entity Type. it has to be OpenChannelJunction    
      enum:    
        - OpenChannelJunction    
      type: string    
      x-ngsi:    
        type: Property    
    uniqueName:    
      description: The name of the junction    
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
    waterInflow:    
      description: Water flow inserted to the junction    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: m3/s    
    waterLevel:    
      description: Water level at the junction    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: m    
    waterOutflow:    
      description: Water flow abstracted from the junction or diverted to another source    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: m3/s    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/OpenChannelJunction/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/OpenChannelJunction/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


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
    "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647"  
  },  
  "downstreamNode": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924",  
  "upstreamNode": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938",  
  "observedBy": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975",  
  "uniqueName": "J1",  
  "tag": "",  
  "waterOutflow": 0.12,  
  "waterInflow": 0.15,  
  "waterLevel": 0.85  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


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
  "waterLevel": {  
    "type": "Number",  
    "value": 0.56  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:OpenChannelJunction:id:PTOM:78370074",  
    "type": "OpenChannelJunction",  
    "address": {  
        "streetAddress": "",  
        "addressLocality": "",  
        "addressRegion": "",  
        "addressCountry": "",  
        "postalCode": "",  
        "postOfficeBoxNumber": ""  
    },  
    "alternateName": "Thivae",  
    "areaServed": "",  
    "dataProvider": "EYDAP",  
    "dateCreated": "1983-10-11T21:04:39Z",  
    "dateModified": "1982-03-03T08:37:57Z",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -65.2981945,  
            -22.649102  
        ]  
    },  
    "name": "J1",  
    "owner": [  
        "urn:ngsi-ld:OpenChannelJunction:items:QPEH:03184806",  
        "urn:ngsi-ld:OpenChannelJunction:items:PUHR:34031741"  
    ],  
    "position": {  
        "distance": 160.6,  
        "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647"  
    },  
    "downstreamNode": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924",  
    "upstreamNode": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938",  
    "observedBy": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975",  
    "uniqueName": "J1",  
    "tag": "",  
    "waterOutflow": 0.12,  
    "waterInflow": 0.15,  
    "waterLevel": 0.85,  
    "seeAlso": [  
        "urn:ngsi-ld:OpenChannelJunction:items:KTWJ:61564622",  
        "urn:ngsi-ld:OpenChannelJunction:items:JOMY:24566116"  
    ],  
    "source": "",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
    ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:OpenChannelJunction:id:PTOM:78370074",  
    "type": "OpenChannelJunction",  
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
        "value": "Thivae"  
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
    "description": {  
        "type": "Property",  
        "value": "Open Channel Junction"  
    },  
    "downstreamNode": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -65.2981945,  
                -22.649102  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "J1"  
    },  
    "observedBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:OpenChannelJunction:items:QPEH:03184806",  
            "urn:ngsi-ld:OpenChannelJunction:items:PUHR:34031741"  
        ]  
    },  
    "position": {  
        "type": "Property",  
        "value": {  
            "distance": 160.6,  
            "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647"  
        }  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:OpenChannelJunction:items:KTWJ:61564622",  
            "urn:ngsi-ld:OpenChannelJunction:items:JOMY:24566116"  
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
    "uniqueName": {  
        "type": "Property",  
        "value": "J1"  
    },  
    "upstreamNode": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938"  
    },  
    "waterInflow": {  
        "type": "Property",  
        "value": 0.15  
    },  
    "waterOutflow": {  
        "type": "Property",  
        "value": 0.12  
    },  
    "waterLevel": {  
        "type": "Property",  
        "value": 0.56  
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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
