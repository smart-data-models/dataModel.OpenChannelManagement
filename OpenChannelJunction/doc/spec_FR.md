Entité : OpenChannelJunction  
============================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/OpenChannelJunction/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Cette entité contient une description harmonisée d'une jonction générique réalisée pour le domaine de gestion du système d'eau brute (canaux ouverts). Une jonction définit un endroit où les caractéristiques du canal changent, où deux ou plusieurs canaux se rejoignent ou se séparent, où des quantités d'eau sont extraites ou insérées dans le système, etc.  
version : 0.0.1  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `downstreamNode`: Une relation indiquant l'ID du nœud en aval (par exemple, la jonction, la structure de régulation), où le canal se termine.  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `observedBy`: Une relation avec l'ID du dispositif qui surveille les propriétés des eaux brutes.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `position`: Objet fournissant des informations sur la distance avec le reste des éléments et une relation avec eux.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `tag`: Une chaîne de texte facultative utilisée pour qualifier un élément  - `type`: propriété. Type d'entité NGSI. Il doit être OpenChannelJunction.  - `uniqueName`: Le nom de la jonction.  - `upstreamNode`: Une relation indiquant l'ID du nœud en amont (par exemple, la jonction, la structure de régulation), où le canal commence.  - `waterInflow`: Flux d'eau inséré à la jonction  - `waterOutflow`: Débit d'eau prélevé à la jonction ou détourné vers une autre source.    
Propriétés requises  
- `id`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OpenChannelJunction:    
  description: 'This entity contains a harmonised description of a generic Junction made for Raw-Water (Open Channels) System Management domain. A Junction defines a location where the characteristics of the channel changes, two or more channels come together or split apart, amounts of water are abstracted or inserted to the system etc.'    
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
    id:    
      anyOf: &openchanneljunction_-_properties_-_owner_-_items_-_anyof    
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
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *openchanneljunction_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    position:    
      description: 'Object providing information about the distance with the rest of the elements and a relationship with them.'    
      properties:    
        distance:    
          description: 'Property. The distance between this Entity and a reference point (e.g., the most upstream point of the system). Units: ''Km'''    
          type: number    
        refPoint:    
          anyOf:    
            - description: 'Property. Identifier format of any NGSI entity.'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity.'    
              format: uri    
              type: string    
          description: 'Relationship. The reference point distance is measured from.'    
      type: object    
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
      description: 'property. NGSI Entity Type. it has to be OpenChannelJunction'    
      enum:    
        - OpenChannelJunction    
      type: string    
    uniqueName:    
      description: 'The name of the junction.'    
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
    waterInflow:    
      description: 'Water flow inserted to the junction'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: m3/s    
    waterOutflow:    
      description: 'Water flow abstracted from the junction or diverted to another source'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: m3/s    
  required:    
    - id    
    - type    
  type: object    
  version: 0.0.1    
```  
</details>    
## Exemples de charges utiles  
#### OpenChannelJunction NGSI-v2 valeurs-clés Exemple  
Voici un exemple d'une OpenChannelJunction au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
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
    "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647",  
    "downstreamNode": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924",  
    "upstreamNode": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938",  
    "observedBy": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975",  
    "uniqueName": "J1",  
    "tag": "",  
    "waterOutflow": 0.12,  
    "waterInflow": 0.15  
  }  
}  
```  
#### OpenChannelJunction NGSI-v2 normalisé Exemple  
Voici un exemple d'une OpenChannelJunction au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### OpenChannelJunction Valeurs clés NGSI-LD Exemple  
Voici un exemple d'une OpenChannelJunction au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
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
    "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647",  
    "downstreamNode": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924",  
    "upstreamNode": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938",  
    "observedBy": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975",  
    "uniqueName": "J1",  
    "tag": "",  
    "waterOutflow": 0.12,  
    "waterInflow": 0.15  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### OpenChannelJunction NGSI-LD normalisé Exemple  
Voici un exemple d'une OpenChannelJunction au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:OpenChannelJunction:id:PTOM:78370074",  
  "type": "OpenChannelJunction",  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -65.2981945,  
        -22.649102  
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
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "J1"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Thivae"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Open Channel Junction"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:OpenChannelJunction:items:QPEH:03184806",  
      "urn:ngsi-ld:OpenChannelJunction:items:PUHR:34031741"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:OpenChannelJunction:items:KTWJ:61564622",  
      "urn:ngsi-ld:OpenChannelJunction:items:JOMY:24566116"  
    ]  
  },  
  "position": {  
    "type": "Property",  
    "value": {  
      "distance": 160.6,  
      "refPoint": "urn:ngsi-ld:OpenChannelJunction:refPoint:JXFD:60487647"  
    }  
  },  
  "downstreamNode": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OpenChannelJunction:downstreamNode:CBWI:21948924"  
  },  
  "upstreamNode": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OpenChannelJunction:upstreamNode:MWGU:81565938"  
  },  
  "observedBy": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OpenChannelJunction:observedBy:GIWE:80160975"  
  },  
  "uniqueName": {  
    "type": "Property",  
    "value": "J1"  
  },  
  "tag": {  
    "type": "Property",  
    "value": ""  
  },  
  "waterOutflow": {  
    "type": "Property",  
    "value": 0.12  
  },  
  "waterInflow": {  
    "type": "Property",  
    "value": 0.15  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
