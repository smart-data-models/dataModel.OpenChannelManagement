Entität: OpenChannel  
====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/OpenChannel/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Einheit enthält eine harmonisierte Beschreibung eines generischen Kanals, der für die Systemmanagement-Domäne Rohwasser (offene Kanäle) erstellt wurde**.  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `bottomSlope`: Die Sohlenneigung des Gerinnes. Alle Einheiten werden im CEFACT-Code akzeptiert.  - `bottomWidth`: Die untere Breite des Gerinnes (bei "trapezförmiger" Geometrie). Alle Einheiten werden im CEFACT-Code akzeptiert.  - `celerity`: Geschwindigkeit eines Schwalls, der sich nach dem Öffnen oder Schließen eines Schleusentors entlang des Gerinnes ausbreitet.  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `diameter`: Der Durchmesser eines kreisförmigen Kanals. Alle Einheiten werden im CEFACT-Code akzeptiert.  - `downstreamNode`: Eine Beziehung, die die ID des nachgelagerten Knotens (z. B. Kreuzung, Regelungsstruktur) angibt, an dem der Kanal endet.  - `flowType`: Text, der die Art der Strömung im Kanal definiert. Enum:'Free-Surface flow'.  - `geometryType`: Die Geometrie des Kanals. Enum:'Trapezförmig, Kreisförmig'].  - `id`: Eindeutiger Bezeichner der Entität  - `leftSideSlope`: Das Gefälle des linken Ufers des Gerinnes (bei "trapezförmiger" Geometrie). Alle Einheiten werden im CEFACT-Code akzeptiert.  - `length`: Die Länge des Kanals. Alle Einheiten werden im CEFACT-Code akzeptiert.  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `maxWaterDepth`: Die maximal zulässige Wassertiefe im Kanal. Alle Einheiten werden im CEFACT-Code akzeptiert.  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `rightSideSlope`: Das Gefälle des rechten Ufers des Gerinnes (bei "trapezförmiger" Geometrie). Alle Einheiten werden im CEFACT-Code akzeptiert.  - `roughnessCoefficient`: Der Manningsche Rauhigkeitskoeffizient.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `tag`: Eine optionale Textzeichenfolge, die zur Qualifizierung einer Position verwendet wird  - `travelDuration`: Die Dauer der Überspannung, die sich vom nachgelagerten Knoten (d. h. der Regelungsstruktur) zum vorgelagerten Knoten bewegt.  - `type`: NGSI-LD Entity Type. es muss OpenChannel sein  - `upstreamNode`: Eine Beziehung, die die ID des vorgelagerten Knotens (z. B. Kreuzung, Regelungsstruktur) angibt, an dem der Kanal beginnt.  - `waterLoss`: Wasserleckagen/-verluste aus dem Kanal - Prozentsatz des Durchflusses des Kanals oder eine Zahl (Durchfluss).    
Erforderliche Eigenschaften  
- `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OpenChannel:    
  description: 'This entity contains a harmonised description of a generic Channel made for Raw-Water (Open Channels) System Management domain.'    
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
    bottomSlope:    
      description: 'The bottom slope of the channel. All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    bottomWidth:    
      description: 'The bottom width of the channel (for ''Trapezoidal'' geometry). All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    celerity:    
      description: 'Velocity of a surge propagated along the channel after the opening or close of a sluice gate.'    
      minimum: 0    
      type: number    
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
      description: 'The diameter of a circular channel. All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    downstreamNode:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of the downstream node (e.g., Junction, Regulation Structure), where the channel ends.'    
      x-ngsi:    
        type: Relationship    
    flowType:    
      description: 'Text defining the type of flow in the channel. Enum:''Free-Surface flow''.'    
      enum:    
        - 'Free-Surface flow'    
      type: string    
      x-ngsi:    
        type: Property    
    geometryType:    
      description: 'The geometry of the channel. Enum:''Trapezoidal, Circular''].'    
      enum:    
        - Circular    
        - Trapezoidal    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &openchannel_-_properties_-_owner_-_items_-_anyof    
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
    leftSideSlope:    
      description: 'The slope of the left bank of the channel (for ''Trapezoidal'' geometry). All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    length:    
      description: 'The length of the channel. All units are accepted in CEFACT code.'    
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
      description: 'The maximum allowable water depth in the channel. All units are accepted in CEFACT code.'    
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
        anyOf: *openchannel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    rightSideSlope:    
      description: 'The slope of the right bank of the channel (for ''Trapezoidal'' geometry). All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    roughnessCoefficient:    
      description: 'The Manning’s roughness coefficient.'    
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
    tag:    
      description: 'An optional text string used to qualify an item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    travelDuration:    
      description: 'The duration of the surge travelling from the downstream node (i.e., Regulation Structure) to the upstream node.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI-LD Entity Type. it has to be OpenChannel'    
      enum:    
        - OpenChannel    
      type: string    
      x-ngsi:    
        type: Property    
    upstreamNode:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of the upstream node (e.g., Junction, Regulation Structure), where the channel begins.'    
      x-ngsi:    
        type: Relationship    
    waterLoss:    
      description: 'Water leakages/losses from the channel - percentage of flow of the channel or a number (flow).'    
      minimum: 0    
      type: object    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### OpenChannel NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen OpenChannel im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### OpenChannel NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen OpenChannel im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### OpenChannel NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen OpenChannel im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### OpenChannel NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen OpenChannel im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Channel:id:IXPY:98787462",  
  "type": "OpenChannel",  
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
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "Section 3"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "S-3"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description of the channel S-3"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": ""  
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
  "areaServed": {  
    "type": "Property",  
    "value": ""  
  },  
  "downstreamNode": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Channel:downstreamNode:DQUS:63966588"  
  },  
  "upstreamNode": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Channel:upstreamNode:MBQH:53312123"  
  },  
  "tag": {  
    "type": "Property",  
    "value": "Something special enjoy research institution past western. System spring clearly impact policy."  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
