Entité : OpenChannelSystem  
==========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/OpenChannelSystem/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Cette entité contient une description harmonisée d'un système générique réalisé pour le domaine de la gestion des systèmes d'eau brute (canaux ouverts). Cette entité représente soit un système composé de différents composants (par exemple, des canaux, des jonctions, des sections transversales, etc.), soit un seul composant (par exemple, un SluiceGate)**.  
version : 0.0.1  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `hasSubSystem`: Référence à une entité de type OpenChannelSystem - un sous-système à canal ouvert.  - `id`: Identifiant unique de l'entité  - `isComposedOf`: Référence aux entités composantes du système de canaux ouverts, de type canal, section transversale, jonction, structure de régulation, vanne, déversoir.  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `mostDownstreamPoint`: Une relation indiquant l'ID du nœud le plus en aval (par exemple, une jonction ou une section transversale) du système.  - `mostUpstreamPoint`: Une relation indiquant l'ID du nœud le plus en amont (par exemple, une jonction ou une section transversale) du système.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type d'entité NGSI-LD. Il doit être OpenChannelSystem    
Propriétés requises  
- `id`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OpenChannelSystem:    
  description: 'This entity contains a harmonised description of a generic system made for Raw-Water (Open Channels) System Management domain. This entity represents either a system composed of different components (e.g., channels, junctions, cross-sections etc.) or just a component (e.g., a SluiceGate).'    
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
    hasSubSystem:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to an entity of type OpenChannelSystem - an open-channel sub-system.'    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: &openchannelsystem_-_properties_-_owner_-_items_-_anyof    
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
    isComposedOf:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the component entities of the open-channel system, of type Channel, Cross-Section, Junction, Regulation Structure, SluiceGate, Spillway.'    
      x-ngsi:    
        type: Relationship    
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
    mostDownstreamPoint:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of the most downstream node (e.g., a Junction or a Cross-section) of the system.'    
      x-ngsi:    
        type: Relationship    
    mostUpstreamPoint:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the ID of the most upstream node (e.g., a Junction or a Cross-section) of the system.'    
      x-ngsi:    
        type: Relationship    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *openchannelsystem_-_properties_-_owner_-_items_-_anyof    
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
    type:    
      description: 'NGSI-LD Entity Type. It has to be OpenChannelSystem'    
      enum:    
        - OpenChannelSystem    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  version: 0.0.1    
```  
</details>    
## Exemples de charges utiles  
#### OpenChannelSystem NGSI-v2 key-values Exemple  
Voici un exemple d'un OpenChannelSystem au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelSystem:id:EHTH:11109231",  
  "type": "OpenChannelSystem",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      59.820118,  
      -157.397178  
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
  "dateCreated": "2020-12-07T21:37:19Z",  
  "dateModified": "2021-07-14T01:06:03Z",  
  "source": "",  
  "name": "L7 - L11",  
  "alternateName": "",  
  "description": "Conveyance System near Thivae",  
  "dataProvider": "EYDAP",  
  "owner": [  
    "urn:ngsi-ld:OpenChannelSystem:items:WPHN:07387656",  
    "urn:ngsi-ld:OpenChannelSystem:items:JNVF:94407376"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:OpenChannelSystem:items:EZUE:70603867",  
    "urn:ngsi-ld:OpenChannelSystem:items:MWLT:38533440"  
  ],  
  "isComposedOf": "urn:ngsi-ld:OpenChannelSystem:isComposedOf:UMLF:11032914",  
  "hasSubSystem": "urn:ngsi-ld:OpenChannelSystem:hasSubSystem:BYUP:86302765",  
  "mostUpstreamPoint": "urn:ngsi-ld:OpenChannelSystem:mostUpstreamPoint:YUHY:75075828",  
  "mostDownstreamPoint": "urn:ngsi-ld:OpenChannelSystem:mostDownstreamPoint:IXHM:68215414"  
}  
```  
#### OpenChannelSystem NGSI-v2 normalisé Exemple  
Voici un exemple d'un OpenChannelSystem au format JSON-LD tel que normalisé. Il est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelSystem:id:EHTH:11109231",  
  "type": "OpenChannelSystem",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        59.820118,  
        -157.397178  
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
    "value": "2020-12-07T21:37:19Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2021-07-14T01:06:03Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "L7 - L11"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "Conveyance System near Thivae"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:OpenChannelSystem:items:WPHN:07387656",  
      "urn:ngsi-ld:OpenChannelSystem:items:JNVF:94407376"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:OpenChannelSystem:items:EZUE:70603867",  
      "urn:ngsi-ld:OpenChannelSystem:items:MWLT:38533440"  
    ]  
  },  
  "isComposedOf": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:OpenChannelSystem:isComposedOf:UMLF:11032914"  
  },  
  "hasSubSystem": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:OpenChannelSystem:hasSubSystem:BYUP:86302765"  
  },  
  "mostUpstreamPoint": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:OpenChannelSystem:mostUpstreamPoint:YUHY:75075828"  
  },  
  "mostDownstreamPoint": {  
    "type": "object",  
    "value": "urn:ngsi-ld:OpenChannelSystem:mostDownstreamPoint:IXHM:68215414"  
  }  
}  
```  
#### Valeurs-clés NGSI-LD de OpenChannelSystem Exemple  
Voici un exemple d'un OpenChannelSystem au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelSystem:id:EHTH:11109231",  
  "type": "OpenChannelSystem",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      59.820118,  
      -157.397178  
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
  "dateCreated": "2020-12-07T21:37:19Z",  
  "dateModified": "2021-07-14T01:06:03Z",  
  "source": "",  
  "name": "L7 - L11",  
  "alternateName": "",  
  "description": "Conveyance System near Thivae",  
  "dataProvider": "EYDAP",  
  "owner": [  
    "urn:ngsi-ld:OpenChannelSystem:items:WPHN:07387656",  
    "urn:ngsi-ld:OpenChannelSystem:items:JNVF:94407376"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:OpenChannelSystem:items:EZUE:70603867",  
    "urn:ngsi-ld:OpenChannelSystem:items:MWLT:38533440"  
  ],  
  "isComposedOf": "urn:ngsi-ld:OpenChannelSystem:isComposedOf:UMLF:11032914",  
  "hasSubSystem": "urn:ngsi-ld:OpenChannelSystem:hasSubSystem:BYUP:86302765",  
  "mostUpstreamPoint": "urn:ngsi-ld:OpenChannelSystem:mostUpstreamPoint:YUHY:75075828",  
  "mostDownstreamPoint": "urn:ngsi-ld:OpenChannelSystem:mostDownstreamPoint:IXHM:68215414",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### OpenChannelSystem NGSI-LD normalisé Exemple  
Voici un exemple d'un OpenChannelSystem au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelSystem:id:EHTH:11109231",  
  "type": "OpenChannelSystem",  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        59.820118,  
        -157.397178  
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
      "@value": "2020-12-07T21:37:19Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-07-14T01:06:03Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "L7 - L11"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": ""  
  },  
  "description": {  
    "type": "Property",  
    "value": "Conveyance System near Thivae"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:OpenChannelSystem:items:WPHN:07387656",  
      "urn:ngsi-ld:OpenChannelSystem:items:JNVF:94407376"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:OpenChannelSystem:items:EZUE:70603867",  
      "urn:ngsi-ld:OpenChannelSystem:items:MWLT:38533440"  
    ]  
  },  
  "isComposedOf": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OpenChannelSystem:isComposedOf:UMLF:11032914"  
  },  
  "hasSubSystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OpenChannelSystem:hasSubSystem:BYUP:86302765"  
  },  
  "mostUpstreamPoint": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OpenChannelSystem:mostUpstreamPoint:YUHY:75075828"  
  },  
  "mostDownstreamPoint": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OpenChannelSystem:mostDownstreamPoint:IXHM:68215414"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
