<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : OpenChannelFlowRegulation    
==================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/OpenChannelFlowRegulation/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Cette entité contient une description harmonisée d'une simulation générique d'une série de structures de régulation indépendantes pour établir des conditions de débit spécifiques dans le système d'adduction. Elle est destinée au domaine de la gestion des systèmes d'eau brute (canaux ouverts).    
version : 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `hasRegulationStructures[array]`: Référence à l'ID d'une entité de type Structure de régulation  - `hasStructuresSimulations[array]`: Référence à l'ID d'une entité de type Structure de régulation Simulation  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `runBy[*]`: L'ID de la personne qui a créé/déclenché la simulation. Référence à une entité de type Utilisateur  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type d'entité NGSI-LD. Il doit s'agir de OpenChannelFlowRegulation  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
OpenChannelFlowRegulation:      
  description: This entity contains a harmonised description of a generic simulation of a series of independent regulation structures to establish specific flow conditions in the conveyance system. It is made for Raw-Water (Open Channels) System Management domain.      
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
    hasRegulationStructures:      
      description: Reference to the ID of an entity of type Regulation structure      
      items:      
        properties:      
          targetURI:      
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
            description: Reference to the ID of an entity of type Regulation structure      
            x-ngsi:      
              type: Relationship      
        type: object      
      type: array      
      x-ngsi:      
        type: Property      
    hasStructuresSimulations:      
      description: Reference to the ID of an entity of type Regulation Structure Simulation      
      items:      
        properties:      
          targetURI:      
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
            description: Reference to the ID of an entity of type Regulation Structure Simulation      
            x-ngsi:      
              type: Relationship      
        type: object      
      type: array      
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
    runBy:      
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
      description: The ID of who created/triggered the simulation. Reference to an entity of type User      
      x-ngsi:      
        type: Relationship      
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
    type:      
      description: NGSI-LD Entity Type. It has to be OpenChannelFlowRegulation      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
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
## Exemples de charges utiles    
#### OpenChannelFlowRegulation Valeurs clés NGSI-v2 Exemple    
Voici un exemple d'une OpenChannelFlowRegulation au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
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
#### OpenChannelFlowRegulation NGSI-v2 normalisé Exemple    
Voici un exemple de OpenChannelFlowRegulation au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
    "type": "Text",  
    "value": "NTUA"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:OpenChannelFlowRegulation:items:XTSQ:90231127",  
      "urn:ngsi-ld:OpenChannelFlowRegulation:items:ULWE:26707834"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
    "value": [  
      {  
        "targetUri": "urn:ngsi-ld:OpenChannelFlowRegulation:hasRegulationStructures:XWXB:83840274"  
      }  
    ]  
  },  
  "hasStructuresSimulations": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "targetUri": "urn:ngsi-ld:OpenChannelFlowRegulation:hasStructuresSimulations:VPDG:92530159"  
      }  
    ]  
  },  
  "runBy": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:OpenChannelFlowRegulation:runBy:CMJE:69885698"  
  }  
}  
```  
</details>    
#### OpenChannelFlowRegulation Valeurs clés NGSI-LD Exemple    
Voici un exemple d'une OpenChannelFlowRegulation au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
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
#### OpenChannelFlowRegulation NGSI-LD normalisé Exemple    
Voici un exemple de OpenChannelFlowRegulation au format JSON-LD tel que normalisé. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
