Entidad: SluiceGate  
===================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/SluiceGate/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Esta entidad contiene una descripción armonizada de una compuerta genérica realizada para el dominio de gestión de sistemas de agua bruta (canales abiertos).**  
versión: 0.0.1  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `curveDischargeCoefficient`: URI de una entidad OpenChannelCurve que representa el coeficiente de descarga (C) en función de la apertura relativa del vertedero (apertura del vertedero (a) sobre la profundidad aguas arriba (H)), C sobre a/H.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `downstreamControlPoint`: Relación que indica el ID de una entidad de tipo Sección Transversal, que representa una sección transversal en una distancia donde las condiciones de flujo son permanentes, aguas abajo de la compuerta.  - `downstreamEndControlPoint`: Relación que indica el ID de una entidad de tipo Sección transversal, que representa una sección transversal justo aguas abajo de la compuerta.  - `flowType`: Define las condiciones de flujo en la puerta. Toma los valores: 'Desbordamiento' (el nivel de agua aguas arriba supera el nivel de la cresta de la compuerta), 'Flujo libre' (el nivel de agua es inferior al borde de la compuerta), 'Flujo sumergido' (el caudal que pasa por la compuerta está regulado por la apertura de la misma). Enum:'Desbordamiento, Flujo Libre, Flujo Sumergido'.  - `gateBottomElevation`: Elevación de la parte inferior (cresta) de la compuerta.  - `gateDischargeCoefficient`: Coeficiente de descarga de la compuerta que tiene en cuenta las pérdidas de energía al pasar el agua por debajo de la compuerta.  - `gateOpening`: La altura de la apertura de la puerta.  - `gateWidth`: La anchura de la esclusa  - `headDifference`: La diferencia entre la profundidad aguas arriba y la profundidad justo aguas abajo.  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `observedBy`: Una relación con el ID del dispositivo que controla las propiedades del agua bruta  - `orificeDischargeCoefficient`: Coeficiente de descarga del orificio que tiene en cuenta las pérdidas de energía a medida que el agua pasa por debajo de la compuerta, y el agua de cola aguas abajo aumenta de manera que la compuerta ya no fluye libremente.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `tag`: Una cadena de texto opcional utilizada para calificar un artículo  - `type`: Tipo de entidad NGSI-LD. Tiene que ser SluiceGate.  - `upstreamControlPoint`: Relación que indica el ID de una entidad de tipo Sección Transversal, que representa una sección transversal en una distancia donde las condiciones de flujo son permanentes, aguas arriba de la compuerta.  - `upstreamEndControlPoint`: Relación que indica el ID de una entidad de tipo Sección transversal, que representa una sección transversal justo aguas arriba de la compuerta.  - `waterDischarge`: La descarga que pasa el vertedero (Q).    
Propiedades requeridas  
- `id`  - `location`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SluiceGate:    
  description: 'This entity contains a harmonised description of a generic Sluice Gate made for Raw-Water (Open Channels) System Management domain.'    
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
    curveDischargeCoefficient:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The URI of an OpenChannelCurve entity that represents the Discharge Coefficient (C) as a function of relative weir opening (weir opening (a) over upstream depth(H)), C over a/H.'    
      x-ngsi:    
        type: Relationship    
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
    downstreamControlPoint:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of an entity of type Cross Section, representing a cross section in a distance where the flow conditions are permanent, downstream of the sluice gate.'    
      x-ngsi:    
        type: Relationship    
    downstreamEndControlPoint:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of an entity of type Cross Section, representing a cross section just downstream of the sluice gate.'    
      x-ngsi:    
        type: Relationship    
    flowType:    
      description: 'It defines the flow conditions in the gate. It takes the values: ''Overflow'' (upstream water level exceeds the weir crest level), ''Free-Flow'' (water level is lower than gate edge), ''Submerged Flow'' (the rate of flow passing through the gate is regulated by the opening of the gate). Enum:''Overflow, Free-Flow, Submerged-Flow''.'    
      enum:    
        - Free-Flow    
        - Overflow    
        - Submerged-Flow    
      type: string    
      x-ngsi:    
        type: Property    
    gateBottomElevation:    
      description: 'Elevation of the bottom (crest) of the gate.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    gateDischargeCoefficient:    
      description: 'Discharge coefficient of the gate that accounts for energy losses as water passes under the gate.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    gateOpening:    
      description: 'The height of gate opening.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    gateWidth:    
      description: 'The width of the sluice gate'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: ' meters.'    
    headDifference:    
      description: 'The difference between the upstream depth and the depth just downstream.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &sluicegate_-_properties_-_owner_-_items_-_anyof    
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
    orificeDischargeCoefficient:    
      description: 'Orifice discharge coefficient that accounts for energy losses as water passes under the gate, and the downstream tailwater increases so that the gate is no longer flowing freely.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *sluicegate_-_properties_-_owner_-_items_-_anyof    
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
    tag:    
      description: 'An optional text string used to qualify an item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It has to be SluiceGate.'    
      enum:    
        - SluiceGate    
      type: string    
      x-ngsi:    
        type: Property    
    upstreamControlPoint:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of an entity of type Cross Section, representing a cross section in a distance where the flow conditions are permanent, upstream of the sluice gate.'    
      x-ngsi:    
        type: Relationship    
    upstreamEndControlPoint:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of an entity of type Cross Section, representing a cross section just upstream of the sluice gate.'    
      x-ngsi:    
        type: Relationship    
    waterDischarge:    
      description: 'The discharge that passes the weir (Q).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
  version: 0.0.1    
```  
</details>    
## Ejemplo de carga útil  
#### SluiceGate NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de una SluiceGate en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:SluiceGate:id:OZDE:42332657",  
  "type": "SluiceGate",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -7.578066,  
      -25.535857  
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
  "dateCreated": "2021-01-13T19:49:28Z",  
  "dateModified": "2021-05-11T14:06:00Z",  
  "source": "",  
  "name": "SG01",  
  "alternateName": "SG01 - Thivae",  
  "description": "Sluic Gate 01 - Thivae",  
  "dataProvider": "EYDAP",  
  "owner": [  
    "urn:ngsi-ld:SluiceGate:items:LXOX:42416570",  
    "urn:ngsi-ld:SluiceGate:items:FSOL:83758025"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SluiceGate:items:ETJS:41829811",  
    "urn:ngsi-ld:SluiceGate:items:IKTE:29167907"  
  ],  
  "tag": "",  
  "gateWidth": 2.5,  
  "gateOpening": 0.5,  
  "gateBottomElevation": 52.3,  
  "gateDischargeCoefficient": 0.5,  
  "orificeDischargeCoefficient": 0.5,  
  "waterDischarge": 9,  
  "headDifference": 1.5,  
  "flowType": "Submerged-Flow",  
  "upstreamEndControlPoint": "urn:ngsi-ld:SluiceGate:upstreamEndControlPoint:JXFD:60487647",  
  "downstreamEndControlPoint": "urn:ngsi-ld:SluiceGate:downstreamEndControlPoint:CBWI:21948924",  
  "upstreamControlPoint": "urn:ngsi-ld:SluiceGate:upstreamControlPoint:MWGU:81565938",  
  "downstreamControlPoint": "urn:ngsi-ld:SluiceGate:downstreamControlPoint:GIWE:80160975",  
  "observedBy": "urn:ngsi-ld:SluiceGate:observedBy:ZWZM:93328711",  
  "curveDischargeCoefficient": "urn:ngsi-ld:SluiceGate:curveDischargeCoefficient:ZPPL:48418583"  
}  
```  
#### SluiceGate NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de una SluiceGate en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:SluiceGate:id:OZDE:42332657",  
  "type": "SluiceGate",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -7.578066,  
        -25.535857  
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
  "dateCreated": {  
      "type": "DateTime",  
      "value": "1972-01-13T19:49:28Z"  
  },  
  "dateModified":  {  
      "type": "DateTime",  
      "value": "2000-05-11T14:06:00Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "SG01"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "SG01 - Thivae"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Sluice Gate 01 - Thivae"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:SluiceGate:items:LXOX:42416570",  
      "urn:ngsi-ld:SluiceGate:items:FSOL:83758025"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:SluiceGate:items:ETJS:41829811",  
      "urn:ngsi-ld:SluiceGate:items:IKTE:29167907"  
    ]  
  },  
  "tag": {  
    "type": "Text",  
    "value": ""  
  },  
  "gateType": {  
    "type": "Text",  
    "value": "Sluice Gate"  
  },  
  "gateWidth": {  
    "type": "Number",  
    "value": 2.5  
  },  
  "gateOpening": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "gateBottomElevation": {  
    "type": "Number",  
    "value": 52.3  
  },  
  "gateDischargeCoefficient": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "orificeDischargeCoefficient": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "waterDischarge": {  
    "type": "Number",  
    "value": 9  
  },  
  "headDifference": {  
    "type": "Number",  
    "value": 1.5  
  },  
  "flowType": {  
    "type": "Text",  
    "value": "Submerged-Flow"  
  },  
  "upstreamEndControlPoint": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:SluiceGate:upstreamEndControlPoint:JXFD:60487647"  
  },  
  "downstreamEndControlPoint": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:SluiceGate:downstreamEndControlPoint:CBWI:21948924"  
  },  
  "upstreamControlPoint": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:SluiceGate:upstreamControlPoint:MWGU:81565938"  
  },  
  "downstreamControlPoint": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SluiceGate:downstreamControlPoint:GIWE:80160975"  
  },  
  "observedBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:SluiceGate:observedBy:ZWZM:93328711"  
  },  
  "curveDischargeCoefficient": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:SluiceGate:curveDischargeCoefficient:ZPPL:48418583"  
  }  
}  
```  
#### SluiceGate NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de una SluiceGate en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:SluiceGate:id:OZDE:42332657",  
  "type": "SluiceGate",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -7.578066,  
      -25.535857  
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
  "dateCreated": "2021-01-13T19:49:28Z",  
  "dateModified": "2021-05-11T14:06:00Z",  
  "source": "",  
  "name": "SG01",  
  "alternateName": "SG01 - Thivae",  
  "description": "Sluic Gate 01 - Thivae",  
  "dataProvider": "EYDAP",  
  "owner": [  
    "urn:ngsi-ld:SluiceGate:items:LXOX:42416570",  
    "urn:ngsi-ld:SluiceGate:items:FSOL:83758025"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SluiceGate:items:ETJS:41829811",  
    "urn:ngsi-ld:SluiceGate:items:IKTE:29167907"  
  ],  
  "tag": "",  
  "gateWidth": 2.5,  
  "gateOpening": 0.5,  
  "gateBottomElevation": 52.3,  
  "gateDischargeCoefficient": 0.5,  
  "orificeDischargeCoefficient": 0.5,  
  "waterDischarge": 9,  
  "headDifference": 1.5,  
  "flowType": "Submerged-Flow",  
  "upstreamEndControlPoint": "urn:ngsi-ld:SluiceGate:upstreamEndControlPoint:JXFD:60487647",  
  "downstreamEndControlPoint": "urn:ngsi-ld:SluiceGate:downstreamEndControlPoint:CBWI:21948924",  
  "upstreamControlPoint": "urn:ngsi-ld:SluiceGate:upstreamControlPoint:MWGU:81565938",  
  "downstreamControlPoint": "urn:ngsi-ld:SluiceGate:downstreamControlPoint:GIWE:80160975",  
  "observedBy": "urn:ngsi-ld:SluiceGate:observedBy:ZWZM:93328711",  
  "curveDischargeCoefficient": "urn:ngsi-ld:SluiceGate:curveDischargeCoefficient:ZPPL:48418583",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### SluiceGate NGSI-LD normalizado Ejemplo  
Este es un ejemplo de una SluiceGate en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:SluiceGate:id:OZDE:42332657",  
  "type": "SluiceGate",  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -7.578066,  
        -25.535857  
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
      "postOfficeBoxNumber": "",  
      "areaServed": ""  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": ""  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1972-01-13T19:49:28Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2000-05-11T14:06:00Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "SG01"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "SG01 - Thivae"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Sluice Gate 01 - Thivae"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SluiceGate:items:LXOX:42416570",  
      "urn:ngsi-ld:SluiceGate:items:FSOL:83758025"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SluiceGate:items:ETJS:41829811",  
      "urn:ngsi-ld:SluiceGate:items:IKTE:29167907"  
    ]  
  },  
  "tag": {  
    "type": "Property",  
    "value": ""  
  },  
  "gateType": {  
    "type": "Property",  
    "value": "Sluice Gate"  
  },  
  "gateWidth": {  
    "type": "Property",  
    "value": 2.5  
  },  
  "gateOpening": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "gateBottomElevation": {  
    "type": "Property",  
    "value": 52.3  
  },  
  "gateDischargeCoefficient": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "orificeDischargeCoefficient": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "waterDischarge": {  
    "type": "Property",  
    "value": 9  
  },  
  "headDifference": {  
    "type": "Property",  
    "value": 1.5  
  },  
  "flowType": {  
    "type": "Property",  
    "value": "Submerged-Flow"  
  },  
  "upstreamEndControlPoint": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SluiceGate:upstreamEndControlPoint:JXFD:60487647"  
  },  
  "downstreamEndControlPoint": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SluiceGate:downstreamEndControlPoint:CBWI:21948924"  
  },  
  "upstreamControlPoint": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SluiceGate:upstreamControlPoint:MWGU:81565938"  
  },  
  "downstreamControlPoint": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SluiceGate:downstreamControlPoint:GIWE:80160975"  
  },  
  "observedBy": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SluiceGate:observedBy:ZWZM:93328711"  
  },  
  "curveDischargeCoefficient": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SluiceGate:curveDischargeCoefficient:ZPPL:48418583"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
