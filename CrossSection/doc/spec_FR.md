Entité : CrossSection  
=====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/CrossSection/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Cette entité contient une description harmonisée d'une section transversale générique réalisée pour le domaine de la gestion des systèmes d'eau brute (canaux ouverts). Une section transversale définit tout point du système où les propriétés de l'eau brute sont surveillées par un dispositif et/ou calculées par simulation**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `attachedTo`: Une relation avec l'ID du canal dans lequel la section transversale "vit". Référence à une entité de type Canal.  - `bottomSlope`: La pente du fond du canal où la section transversale "vit". Toutes les unités sont acceptées en code CEFACT.  - `bottomWidth`: La largeur inférieure de la section transversale (pour la géométrie "trapézoïdale"). Toutes les unités sont acceptées dans le code CEFACT.  - `crossSectionGeometry`: La géométrie de la section transversale. Enum : 'Circulaire, Trapézoïdale'.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `diameter`: Le diamètre d'une section transversale circulaire.  - `energyHead`: La tête d'énergie totale à la section transversale.  - `id`: Identifiant unique de l'entité  - `inheritsFrom`: URI d'un composant du canal à partir duquel la valeur d'une propriété est obtenue.  - `leftSideSlope`: La pente de la rive gauche de la section transversale (pour la géométrie "trapézoïdale"). Toutes les unités sont acceptées en code CEFACT.  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `maxWaterDepth`: La profondeur d'eau maximale admissible au niveau de la section transversale. Toutes les unités sont acceptées en code CEFACT.  - `name`: Le nom de cet élément.  - `observedBy`: Une relation avec l'ID du dispositif qui surveille les propriétés des eaux brutes.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `position`: Objet fournissant des informations sur la distance avec le reste des éléments et une relation avec eux.  - `rightSideSlope`: La pente de la rive droite de la section transversale (pour la géométrie "trapézoïdale"). Toutes les unités sont acceptées en code CEFACT.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `specificConductivity`: Conductivité de l'eau au niveau de la section transversale.  - `tag`: Une chaîne de texte facultative utilisée pour qualifier un élément  - `turbidity`: Turbidité de l'eau à la section transversale.  - `type`: Type d'entité NGSI-LD. Il doit s'agir de CrossSection.  - `waterFlow`: Ecoulement de l'eau au niveau de la section transversale.  - `waterLevel`: Niveau d'eau à la section transversale.  - `waterTemperature`: Température de l'eau au niveau de la section transversale.  - `waterVelocity`: Vitesse de l'eau à la section transversale.    
Propriétés requises  
- `id`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CrossSection:    
  description: 'This entity contains a harmonised description of a generic Cross-Section made for Raw-Water (Open Channels) System Management domain. A CrossSection defines any point of the system where raw-water properties are monitored by a device and/or computed via simulation.'    
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
    attachedTo:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship to the ID of the channel where the cross-section ''lives in''. Reference to an entity of type Channel.'    
      x-ngsi:    
        type: Relationship    
    bottomSlope:    
      description: 'The bottom slope of the channel where the cross-section ''lives in''. All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    bottomWidth:    
      description: 'The bottom width of the cross-section (for ''Trapezoidal'' geometry). All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    crossSectionGeometry:    
      description: 'The geometry of the cross-section. Enum:''Circular, Trapezoidal''.'    
      enum:    
        - Circular    
        - Trapezoidal    
      type: string    
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
      description: 'The diameter of a circular cross-section.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    energyHead:    
      description: 'The total energy head at the cross-section.'    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &crosssection_-_properties_-_owner_-_items_-_anyof    
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
    inheritsFrom:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'URI of a Channel component from which the value of a property is obtained.'    
      x-ngsi:    
        type: Relationship    
    leftSideSlope:    
      description: 'The slope of the left bank of the cross-section (for ''Trapezoidal'' geometry). All units are accepted in CEFACT code.'    
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
      description: 'The maximum allowable water depth at the cross-section. All units are accepted in CEFACT code.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
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
        anyOf: *crosssection_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    position:    
      description: 'Object providing information about the distance with the rest of the elements and a relationship with them.'    
      properties:    
        distance:    
          description: 'Property. The distance between this Entity and a reference point (e.g., the most upstream point of the system).'    
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
    rightSideSlope:    
      description: 'The slope of the right bank of the cross-section (for ''Trapezoidal'' geometry). All units are accepted in CEFACT code.'    
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
    specificConductivity:    
      description: 'Water conductivity at the cross-section.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    tag:    
      description: 'An optional text string used to qualify an item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    turbidity:    
      description: 'Water turbidity at the cross-section.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It has to be CrossSection.'    
      enum:    
        - CrossSection    
      type: string    
      x-ngsi:    
        type: Property    
    waterFlow:    
      description: 'Water flow at the cross-section.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    waterLevel:    
      description: 'Water level at the cross-section.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    waterTemperature:    
      description: 'Water temperature at the cross-section.'    
      type: number    
      x-ngsi:    
        type: Property    
    waterVelocity:    
      description: 'Water Velocity at the cross-section.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### CrossSection NGSI-v2 valeurs-clés Exemple  
Voici un exemple de CrossSection au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CrossSection:id:COGE:70479090",  
  "type": "CrossSection",  
  "dateCreated": "1990-11-25T18:54:15Z",  
  "dateModified": "1999-04-24T10:03:17Z",  
  "source": "",  
  "name": "L3",  
  "alternateName": "Giona",  
  "description": "Giona 1",  
  "dataProvider": "",  
  "owner": [  
    "urn:ngsi-ld:CrossSection:items:ILNP:15826171",  
    "urn:ngsi-ld:CrossSection:items:RUEP:96519173"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:CrossSection:items:GEPQ:35001404",  
    "urn:ngsi-ld:CrossSection:items:YRBN:14719571"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      28.7415145,  
      -31.163341  
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
  "attachedTo": "urn:ngsi-ld:CrossSection:attachedTo:CTHP:74683243",  
  "observedBy": "urn:ngsi-ld:CrossSection:observedBy:WJTI:74120377",  
  "tag": "",  
  "position": {  
    "distance": 864.6,  
    "refPoint": "urn:ngsi-ld:CrossSection:refPoint:JXFD:60487647"  
  },  
  "waterFlow": 12,  
  "waterVelocity": 0.082,  
  "waterTemperature": 9.6,  
  "turbidity": 11.8,  
  "specificConductivity": 260,  
  "waterLevel": 2.9,  
  "energyHead": 0.032,  
  "crossSectionGeometry": "Trapezoidal",  
  "bottomSlope": 0.02,  
  "leftSideSlope": 0.02,  
  "rightSideSlope": 0.02,  
  "bottomWidth": 5,  
  "diameter": 0,  
  "maxWaterDepth": 4,  
  "inheritsFrom": "urn:ngsi-ld:CrossSection:inheritsFrom:JXFD:60487647"  
}  
```  
#### Section transversale normalisée NGSI-v2 Exemple  
Voici un exemple de CrossSection au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CrossSection:id:COGE:70479090",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1990-11-25T18:54:15Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1999-04-24T10:03:17Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "L3"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Giona"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Giona 1"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": ""  
  },  
  "owner": {  
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:CrossSection:items:ILNP:15826171",  
      "urn:ngsi-ld:CrossSection:items:RUEP:96519173"  
    ]  
  },  
  "seeAlso": {  
    "type": "Array",  
    "value": [  
      "urn:ngsi-ld:CrossSection:items:GEPQ:35001404",  
      "urn:ngsi-ld:CrossSection:items:YRBN:14719571"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        28.7415145,  
        -31.163341  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredObject",  
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
  "type": "CrossSection",  
  "attachedTo": {  
    "type": "object",  
    "value": "urn:ngsi-ld:CrossSection:attachedTo:CTHP:74683243"  
  },  
  "observedBy": {  
    "type": "object",  
    "value": "urn:ngsi-ld:CrossSection:observedBy:WJTI:74120377"  
  },  
  "tag": {  
    "type": "Text",  
    "value": ""  
  },  
  "position": {  
    "type": "StructuredObject",  
    "value": {  
      "distance": 864.6,  
      "refPoint": "urn:ngsi-ld:CrossSection:refPoint:JXFD:60487647"  
    }  
  },  
  "waterFlow": {  
    "type": "Number",  
    "value": 12  
  },  
  "waterVelocity": {  
    "type": "Number",  
    "value": 0.082  
  },  
  "waterTemperature": {  
    "type": "Number",  
    "value": 9.6  
  },  
  "turbidity": {  
    "type": "Number",  
    "value": 11.8  
  },  
  "specificConductivity": {  
    "type": "Number",  
    "value": 260  
  },  
  "waterLevel": {  
    "type": "Number",  
    "value": 2.9  
  },  
  "energyHead": {  
    "type": "Number",  
    "value": 0.032  
  },  
  "crossSectionGeometry": {  
    "type": "Text",  
    "value": "Trapezoidal"  
  },  
  "bottomSlope": {  
    "type": "Number",  
    "value": 0.02  
  },  
  "leftSideSlope": {  
    "type": "Number",  
    "value": 0.02  
  },  
  "rightSideSlope": {  
    "type": "Number",  
    "value": 0.02  
  },  
  "bottomWidth": {  
    "type": "Number",  
    "value": 5  
  },  
  "diameter": {  
    "type": "Number",  
    "value": 0  
  },  
  "maxWaterDepth": {  
    "type": "Number",  
    "value": 4  
  },  
  "inheritsFrom": {  
    "type": "object",  
    "value": "urn:ngsi-ld:CrossSection:inheritsFrom:JXFD:60487647"  
  }  
}  
```  
#### Section transversale des valeurs clés NGSI-LD Exemple  
Voici un exemple de CrossSection au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CrossSection:id:COGE:70479090",  
  "type": "CrossSection",  
  "dateCreated": "1990-11-25T18:54:15Z",  
  "dateModified": "1999-04-24T10:03:17Z",  
  "source": "",  
  "name": "L3",  
  "alternateName": "Giona",  
  "description": "Giona 1",  
  "dataProvider": "",  
  "owner": [  
    "urn:ngsi-ld:CrossSection:items:ILNP:15826171",  
    "urn:ngsi-ld:CrossSection:items:RUEP:96519173"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:CrossSection:items:GEPQ:35001404",  
    "urn:ngsi-ld:CrossSection:items:YRBN:14719571"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      28.7415145,  
      -31.163341  
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
  "attachedTo": "urn:ngsi-ld:CrossSection:attachedTo:CTHP:74683243",  
  "observedBy": "urn:ngsi-ld:CrossSection:observedBy:WJTI:74120377",  
  "tag": "",  
  "position": {  
    "distance": 864.6,  
    "refPoint": "urn:ngsi-ld:CrossSection:refPoint:JXFD:60487647"  
  },  
  "waterFlow": 12,  
  "waterVelocity": 0.082,  
  "waterTemperature": 9.6,  
  "turbidity": 11.8,  
  "specificConductivity": 260,  
  "waterLevel": 2.9,  
  "energyHead": 0.032,  
  "crossSectionGeometry": "Trapezoidal",  
  "bottomSlope": 0.02,  
  "leftSideSlope": 0.02,  
  "rightSideSlope": 0.02,  
  "bottomWidth": 5,  
  "diameter": 0,  
  "maxWaterDepth": 4,  
  "inheritsFrom": "urn:ngsi-ld:CrossSection:inheritsFrom:JXFD:60487647",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### Section transversale normalisée NGSI-LD Exemple  
Voici un exemple de CrossSection au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CrossSection:id:COGE:70479090",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1990-11-25T18:54:15Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1999-04-24T10:03:17Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "L3"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Giona"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Giona 1"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": ""  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:CrossSection:items:ILNP:15826171",  
      "urn:ngsi-ld:CrossSection:items:RUEP:96519173"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:CrossSection:items:GEPQ:35001404",  
      "urn:ngsi-ld:CrossSection:items:YRBN:14719571"  
    ]  
  },  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        28.7415145,  
        -31.163341  
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
  "type": "CrossSection",  
  "attachedTo": {  
    "type": "object",  
    "value": "urn:ngsi-ld:CrossSection:attachedTo:CTHP:74683243"  
  },  
  "observedBy": {  
    "type": "object",  
    "value": "urn:ngsi-ld:CrossSection:observedBy:WJTI:74120377"  
  },  
  "tag": {  
    "type": "Property",  
    "value": ""  
  },  
  "position": {  
    "type": "Property",  
    "value": {  
      "distance": 864.6,  
      "refPoint": "urn:ngsi-ld:CrossSection:refPoint:JXFD:60487647"  
    }  
  },  
  "waterFlow": {  
    "type": "Property",  
    "value": 12  
  },  
  "waterVelocity": {  
    "type": "Property",  
    "value": 0.082  
  },  
  "waterTemperature": {  
    "type": "Property",  
    "value": 9.6  
  },  
  "turbidity": {  
    "type": "Property",  
    "value": 11.8  
  },  
  "specificConductivity": {  
    "type": "Property",  
    "value": 260  
  },  
  "waterLevel": {  
    "type": "Property",  
    "value": 2.9  
  },  
  "energyHead": {  
    "type": "Property",  
    "value": 0.032  
  },  
  "crossSectionGeometry": {  
    "type": "Property",  
    "value": "Trapezoidal"  
  },  
  "bottomSlope": {  
    "type": "Property",  
    "value": 0.02  
  },  
  "leftSideSlope": {  
    "type": "Property",  
    "value": 0.02  
  },  
  "rightSideSlope": {  
    "type": "Property",  
    "value": 0.02  
  },  
  "bottomWidth": {  
    "type": "Property",  
    "value": 5  
  },  
  "diameter": {  
    "type": "Property",  
    "value": 0  
  },  
  "maxWaterDepth": {  
    "type": "Property",  
    "value": 4  
  },  
  "inheritsFrom": {  
    "type": "object",  
    "value": "urn:ngsi-ld:CrossSection:inheritsFrom:JXFD:60487647"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude