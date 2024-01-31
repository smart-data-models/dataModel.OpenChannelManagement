<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: RegulaciónEstructura    
=============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/RegulationStructure/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Esta entidad contiene una descripción armonizada de una Estructura de Regulación genérica realizada para el dominio de Gestión del Sistema de Agua Cruda (Canales Abiertos). La estructura de regulación representa un objeto de tipo empalme, que controla el flujo de agua en el sistema de agua bruta**.    
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
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `hasSluiceGate[*]`: Referencia a una entidad de tipo Esclusa  - `hasSpillway[*]`: Referencia a una entidad de tipo Esclusa Vertedero  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `numberOfGates[number]`: Valor entero que define el número de puertas de control conectadas a la estructura de regulación.  - `numberOfSpillways[number]`: Valor entero que define el número de aliviaderos conectados a la estructura de regulación.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `position[object]`: Objeto que proporciona información sobre la distancia con el resto de elementos y una relación con ellos  	- `distance[number]`: Distancia entre esta Entidad y un punto de referencia (por ejemplo, el punto más aguas arriba del sistema).      
- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `tag[string]`: Cadena de texto opcional utilizada para calificar un elemento  . Model: [https://schema.org/Text](https://schema.org/Text)- `teleCommand[boolean]`: Defina si la estructura de regulación se controla a distancia o manualmente. Valor verdadero/falso  - `type[string]`: Tipo de entidad NGSI-LD. Tiene que ser RegulationStructure  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
RegulationStructure:      
  description: 'This entity contains a harmonised description of a generic Regulation Structure made for Raw-Water (Open Channels) System Management domain. Regulation structure represents a junction-type object, controlling the water flow in the raw-water system.'      
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
    hasSluiceGate:      
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
      description: Reference to an entity of type Sluice gate      
      x-ngsi:      
        type: Relationship      
    hasSpillway:      
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
      description: Reference to an entity of type Sluice gate Spillway      
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
    numberOfGates:      
      description: An integer value defining the number of control gates attached to the regulation structure      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    numberOfSpillways:      
      description: An integer value defining the number of spillways attached to the regulation structure      
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
    position:      
      description: Object providing information about the distance with the rest of the elements and a relationship with them      
      properties:      
        distance:      
          description: 'The distance between this Entity and a reference point (e.g., the most upstream point of the system)'      
          type: number      
          x-ngsi:      
            type: Property      
            units: 'Km '      
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
    teleCommand:      
      description: Define whether the regulation structure is controlled remotely or manually. True/False value      
      type: boolean      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI-LD Entity Type. It has to be RegulationStructure      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
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
## Ejemplo de carga útil    
#### RegulationStructure NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de una RegulationStructure en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
  }  
}  
```  
</details>    
#### RegulationStructure NGSI-v2 normalized Ejemplo    
He aquí un ejemplo de una RegulationStructure en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
    "type": "StructuredValue",  
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
    "type": "Text",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:RegulationStructure:items:ASWJ:21246595",  
      "urn:ngsi-ld:RegulationStructure:items:NHFZ:56673870"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
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
    "type": "Boolean",  
    "value": true  
  },  
  "numberOfSpillways": {  
    "type": "Boolean",  
    "value": true  
  },  
  "teleCommand": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasSluiceGate": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:RegulationStructure:hasSluiceGate:JXFD:60487647"  
  },  
  "hasSpillway": {  
    "type": "Text",  
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
#### RegulationStructure NGSI-LD key-values Ejemplo    
He aquí un ejemplo de una RegulationStructure en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### RegulaciónEstructura NGSI-LD normalizada Ejemplo    
He aquí un ejemplo de una RegulationStructure en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
        "type": "GeoProperty",  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
