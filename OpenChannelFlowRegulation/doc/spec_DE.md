<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: OpenChannelFlowRegulation  
==================================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/OpenChannelFlowRegulation/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Diese Einheit enthält eine harmonisierte Beschreibung einer generischen Simulation einer Reihe unabhängiger Regelungsstrukturen zur Festlegung spezifischer Durchflussbedingungen in einem Transportsystem. Sie ist für die Domäne Rohwasser (offene Kanäle) Systemmanagement bestimmt.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `hasRegulationStructures[array]`: Verweis auf die ID einer Entität vom Typ Regelstruktur  - `hasStructuresSimulations[array]`: Verweis auf die ID einer Entität vom Typ Regelungsstruktur Simulation  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `runBy[*]`: Die ID desjenigen, der die Simulation erstellt/ausgelöst hat. Referenz auf eine Entität des Typs Benutzer  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI-LD-Entitätstyp. Es muss OpenChannelFlowRegulation sein.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OpenChannelFlowRegulation:    
  description: 'This entity contains a harmonised description of a generic simulation of a series of independent regulation structures to establish specific flow conditions in the conveyance system. It is made for Raw-Water (Open Channels) System Management domain.'    
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
    hasRegulationStructures:    
      description: 'Reference to the ID of an entity of type Regulation structure'    
      items:    
        properties:    
          targetURI:    
            anyOf:    
              - description: 'Property. Identifier format of any NGSI entity'    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              - description: 'Property. Identifier format of any NGSI entity'    
                format: uri    
                type: string    
            description: 'Relationship. Reference to the ID of an entity of type Regulation structure'    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    hasStructuresSimulations:    
      description: 'Reference to the ID of an entity of type Regulation Structure Simulation'    
      items:    
        properties:    
          targetURI:    
            anyOf:    
              - description: 'Property. Identifier format of any NGSI entity'    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              - description: 'Property. Identifier format of any NGSI entity'    
                format: uri    
                type: string    
            description: 'Relationship. Reference to the ID of an entity of type Regulation Structure Simulation'    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &openchannelflowregulation_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *openchannelflowregulation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    runBy:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The ID of who created/triggered the simulation. Reference to an entity of type User'    
      x-ngsi:    
        type: Relationship    
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
      description: 'NGSI-LD Entity Type. It has to be OpenChannelFlowRegulation.'    
      enum:    
        - OpenChannelFlowRegulation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/OpenChannelFlowRegulation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/OpenChannelFlowRegulation/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### OpenChannelFlowRegulation NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine OpenChannelFlowRegulation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelFlowRegulation:id:YLKZ:61350129",  
  "type": "OpenChannelFlowRegulation",  
  "dateCreated": "2017-05-04T03:59:29Z",  
  "dateModified": "2005-01-20T20:06:38Z",  
  "source": "",  
  "name": "Simulation_Scenario_1",  
  "alternateName": "Simulation Scenario 1",  
  "description": "Results of Simulation Scenario 1",  
  "dataProvider": "NTUA",  
  "owner": [  
    "urn:ngsi-ld:OpenChannelFlowRegulation:items:XTSQ:90231127",  
    "urn:ngsi-ld:OpenChannelFlowRegulation:items:ULWE:26707834"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:OpenChannelFlowRegulation:items:HJOC:81615506",  
    "urn:ngsi-ld:OpenChannelFlowRegulation:items:BHCJ:50756499"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      57.412865,  
      -128.395711  
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
  "hasRegulationStructures": [  
    {  
      "targetUri": "urn:ngsi-ld:OpenChannelFlowRegulation:hasRegulationStructures:XWXB:83840274"  
    }  
  ],  
  "hasStructuresSimulations": [  
    {  
      "targetUri": "urn:ngsi-ld:OpenChannelFlowRegulation:hasStructuresSimulations:VPDG:92530159"  
    }  
  ],  
  "runBy": "urn:ngsi-ld:OpenChannelFlowRegulation:runBy:CMJE:69885698"  
}  
```  
</details>  
#### OpenChannelFlowRegulation NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine OpenChannelFlowRegulation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelFlowRegulation:id:YLKZ:61350129",  
  "type": "OpenChannelFlowRegulation",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-05-04T03:59:29Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2005-01-20T20:06:38Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Simulation_Scenario_1"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Simulation Scenario 1"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Results of Simulation Scenario 1"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "NTUA"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:OpenChannelFlowRegulation:items:XTSQ:90231127",  
      "urn:ngsi-ld:OpenChannelFlowRegulation:items:ULWE:26707834"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:OpenChannelFlowRegulation:items:HJOC:81615506",  
      "urn:ngsi-ld:OpenChannelFlowRegulation:items:BHCJ:50756499"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        57.412865,  
        -128.395711  
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
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": ""  
  },  
  "hasRegulationStructures": {  
    "type": "array",  
    "value": [  
      {  
        "targetUri": "urn:ngsi-ld:OpenChannelFlowRegulation:hasRegulationStructures:XWXB:83840274"  
      }  
    ]  
  },  
  "hasStructuresSimulations": {  
    "type": "array",  
    "value": [  
      {  
        "targetUri": "urn:ngsi-ld:OpenChannelFlowRegulation:hasStructuresSimulations:VPDG:92530159"  
      }  
    ]  
  },  
  "runBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:OpenChannelFlowRegulation:runBy:CMJE:69885698"  
  }  
}  
```  
</details>  
#### OpenChannelFlowRegulation NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine OpenChannelFlowRegulation im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:OpenChannelFlowRegulation:id:YLKZ:61350129",  
    "type": "OpenChannelFlowRegulation",  
    "address": {  
        "streetAddress": "",  
        "addressLocality": "",  
        "addressRegion": "",  
        "addressCountry": "",  
        "postalCode": "",  
        "postOfficeBoxNumber": ""  
    },  
    "alternateName": "Simulation Scenario 1",  
    "areaServed": "",  
    "dataProvider": "NTUA",  
    "dateCreated": "2017-05-04T03:59:29Z",  
    "dateModified": "2005-01-20T20:06:38Z",  
    "description": "Results of Simulation Scenario 1",  
    "hasRegulationStructures": [  
        {  
            "targetUri": "urn:ngsi-ld:OpenChannelFlowRegulation:hasRegulationStructures:XWXB:83840274"  
        }  
    ],  
    "hasStructuresSimulations": [  
        {  
            "targetUri": "urn:ngsi-ld:OpenChannelFlowRegulation:hasStructuresSimulations:VPDG:92530159"  
        }  
    ],  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            57.412865,  
            -128.395711  
        ]  
    },  
    "name": "Simulation_Scenario_1",  
    "owner": [  
        "urn:ngsi-ld:OpenChannelFlowRegulation:items:XTSQ:90231127",  
        "urn:ngsi-ld:OpenChannelFlowRegulation:items:ULWE:26707834"  
    ],  
    "runBy": "urn:ngsi-ld:OpenChannelFlowRegulation:runBy:CMJE:69885698",  
    "seeAlso": [  
        "urn:ngsi-ld:OpenChannelFlowRegulation:items:HJOC:81615506",  
        "urn:ngsi-ld:OpenChannelFlowRegulation:items:BHCJ:50756499"  
    ],  
    "source": "",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### OpenChannelFlowRegulation NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine OpenChannelFlowRegulation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:OpenChannelFlowRegulation:id:YLKZ:61350129",  
    "type": "OpenChannelFlowRegulation",  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "",  
            "addressLocality": "",  
            "addressRegion": "",  
            "addressCountry": "",  
            "postalCode": "",  
            "postOfficeBoxNumber": ""  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "Simulation Scenario 1"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "NTUA"  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2017-05-04T03:59:29Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2005-01-20T20:06:38Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Results of Simulation Scenario 1"  
    },  
    "hasRegulationStructures": {  
        "type": "Property",  
        "value": [  
            {  
                "targetUri": "urn:ngsi-ld:OpenChannelFlowRegulation:hasRegulationStructures:XWXB:83840274"  
            }  
        ]  
    },  
    "hasStructuresSimulations": {  
        "type": "Property",  
        "value": [  
            {  
                "targetUri": "urn:ngsi-ld:OpenChannelFlowRegulation:hasStructuresSimulations:VPDG:92530159"  
            }  
        ]  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                57.412865,  
                -128.395711  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Simulation_Scenario_1"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:OpenChannelFlowRegulation:items:XTSQ:90231127",  
            "urn:ngsi-ld:OpenChannelFlowRegulation:items:ULWE:26707834"  
        ]  
    },  
    "runBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:OpenChannelFlowRegulation:runBy:CMJE:69885698"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:OpenChannelFlowRegulation:items:HJOC:81615506",  
            "urn:ngsi-ld:OpenChannelFlowRegulation:items:BHCJ:50756499"  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
