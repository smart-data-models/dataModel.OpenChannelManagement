<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: OpenChannelCurve  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/OpenChannelCurve/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Esta entidad contiene una descripción armonizada de una curva genérica realizada para el ámbito de la gestión de sistemas de agua bruta (canales abiertos)**.  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local    
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `curveType[string]`: Tipo de curva para aliviaderos y estructuras de regulación. Puede ser una curva que represente 1) el coeficiente de descarga (C) en función de la abertura relativa del vertedero (a/H, a: abertura de la compuerta, H: altura aguas arriba), 2) el caudal (Q) en función de la altura del agua (H), 3) el coeficiente de caudal de proyecto (Co) en función de P/Ho, donde P es la altura de la plataforma del aliviadero OGEE y Ho la altura aguas arriba de proyecto, 4) el coeficiente de caudal (C) en función de H/L, donde H es la altura aguas arriba y L la longitud de un aliviadero ABIERTO-CRESTADO, 5) la función C/Co - H/Ho. Enum:'C-a/H, H-Q, Co-P/Ho, C-H/L, C/Co-H/Ho'  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `tag[string]`: Cadena de texto opcional utilizada para calificar un elemento  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo de entidad NGSI. Tiene que ser OpenChannelCurve  - `xData[array]`: X puntos de datos para la curva  - `yData[array]`: Puntos de datos Y para la curva  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OpenChannelCurve:    
  description: This entity contains a harmonised description of a generic curve made for Raw-Water (Open Channels) System Management domain.    
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
    tag:    
      description: An optional text string used to qualify an item    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity Type. It has to be OpenChannelCurve    
      enum:    
        - OpenChannelCurve    
      type: string    
      x-ngsi:    
        type: Property    
    xData:    
      description: X data points for the curve    
      items:    
        type: number    
      type: array    
      x-ngsi:    
        type: Property    
    yData:    
      description: Y data points for the curve    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
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
## Ejemplo de carga útil  
#### OpenChannelCurve NGSI-v2 key-values Ejemplo  
He aquí un ejemplo de una OpenChannelCurve en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### OpenChannelCurve NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de OpenChannelCurve en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### OpenChannelCurve NGSI-LD key-values Ejemplo  
He aquí un ejemplo de una OpenChannelCurve en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### OpenChannelCurve NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de OpenChannelCurve en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
