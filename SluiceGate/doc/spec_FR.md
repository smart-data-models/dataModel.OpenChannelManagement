<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : SluiceGate  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/SluiceGate/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Cette entité contient une description harmonisée d'une vanne générique destinée à la gestion des systèmes d'eau brute (canaux ouverts).  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `curveDischargeCoefficient[*]`: L'URI d'une entité OpenChannelCurve qui représente le coefficient de débit (C) en fonction de l'ouverture relative du déversoir (ouverture du déversoir (a) sur la profondeur amont (H)), C sur a/H  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `downstreamControlPoint[*]`: Une relation indiquant l'ID d'une entité de type Section transversale, représentant une section transversale sur une distance où les conditions d'écoulement sont permanentes, en aval de la vanne.  - `downstreamEndControlPoint[*]`: Une relation indiquant l'ID d'une entité de type Section transversale, représentant une section transversale juste en aval de la vanne.  - `flowType[string]`: Il définit les conditions d'écoulement dans la porte. Il prend les valeurs suivantes 'Débordement' (le niveau d'eau en amont dépasse le niveau de la crête du déversoir), 'Ecoulement libre' (le niveau d'eau est inférieur au bord de la vanne), 'Ecoulement submergé' (le débit passant par la vanne est régulé par l'ouverture de la vanne). Enum : "Déversement, écoulement libre, écoulement submergé".  - `gateBottomElevation[number]`: Élévation du fond (crête) de la vanne  - `gateDischargeCoefficient[number]`: Coefficient de décharge de la vanne qui tient compte des pertes d'énergie lorsque l'eau passe sous la vanne  - `gateOpening[number]`: La hauteur de l'ouverture du portail  - `gateWidth[number]`: La largeur de la vanne  - `headDifference[number]`: La différence entre la profondeur en amont et la profondeur juste en aval  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `observedBy[*]`: Une relation avec l'ID de l'appareil qui surveille les propriétés de l'eau brute  . Model: [https://smart-data-models.github.io/dataModel.Device/device-schema.json](https://smart-data-models.github.io/dataModel.Device/device-schema.json)- `orificeDischargeCoefficient[number]`: Coefficient de débit de l'orifice qui tient compte des pertes d'énergie lorsque l'eau passe sous la vanne et que le débit de fuite en aval augmente de sorte que la vanne ne s'écoule plus librement.  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `tag[string]`: Une chaîne de texte facultative utilisée pour qualifier un élément  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Type d'entité NGSI-LD. Il doit s'agir de SluiceGate  - `upstreamControlPoint[*]`: Une relation indiquant l'ID d'une entité de type Section transversale, représentant une section transversale sur une distance où les conditions d'écoulement sont permanentes, en amont de la vanne.  - `upstreamEndControlPoint[*]`: Une relation indiquant l'ID d'une entité de type Section transversale, représentant une section transversale juste en amont de la vanne.  - `waterDischarge[number]`: Le débit qui passe le déversoir (Q)  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SluiceGate:    
  description: This entity contains a harmonised description of a generic Sluice Gate made for Raw-Water (Open Channels) System Management domain.    
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
    curveDischargeCoefficient:    
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
      description: 'The URI of an OpenChannelCurve entity that represents the Discharge Coefficient (C) as a function of relative weir opening (weir opening (a) over upstream depth(H)), C over a/H'    
      x-ngsi:    
        type: Relationship    
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
    downstreamControlPoint:    
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
      description: 'A relationship indicating the ID of an entity of type Cross Section, representing a cross section in a distance where the flow conditions are permanent, downstream of the sluice gate'    
      x-ngsi:    
        type: Relationship    
    downstreamEndControlPoint:    
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
      description: 'A relationship indicating the ID of an entity of type Cross Section, representing a cross section just downstream of the sluice gate'    
      x-ngsi:    
        type: Relationship    
    flowType:    
      description: 'It defines the flow conditions in the gate. It takes the values: ''Overflow'' (upstream water level exceeds the weir crest level), ''Free-Flow'' (water level is lower than gate edge), ''Submerged Flow'' (the rate of flow passing through the gate is regulated by the opening of the gate). Enum:''Overflow, Free-Flow, Submerged-Flow'''    
      enum:    
        - Free-Flow    
        - Overflow    
        - Submerged-Flow    
      type: string    
      x-ngsi:    
        type: Property    
    gateBottomElevation:    
      description: Elevation of the bottom (crest) of the gate    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    gateDischargeCoefficient:    
      description: Discharge coefficient of the gate that accounts for energy losses as water passes under the gate    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    gateOpening:    
      description: The height of gate opening    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    gateWidth:    
      description: The width of the sluice gate    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: ' meters'    
    headDifference:    
      description: The difference between the upstream depth and the depth just downstream    
      minimum: 0    
      type: number    
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
    orificeDischargeCoefficient:    
      description: 'Orifice discharge coefficient that accounts for energy losses as water passes under the gate, and the downstream tailwater increases so that the gate is no longer flowing freely'    
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
      description: NGSI-LD Entity Type. It has to be SluiceGate    
      enum:    
        - SluiceGate    
      type: string    
      x-ngsi:    
        type: Property    
    upstreamControlPoint:    
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
      description: 'A relationship indicating the ID of an entity of type Cross Section, representing a cross section in a distance where the flow conditions are permanent, upstream of the sluice gate'    
      x-ngsi:    
        type: Relationship    
    upstreamEndControlPoint:    
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
      description: 'A relationship indicating the ID of an entity of type Cross Section, representing a cross section just upstream of the sluice gate'    
      x-ngsi:    
        type: Relationship    
    waterDischarge:    
      description: The discharge that passes the weir (Q)    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/SluiceGate/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/SluiceGate/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### SluiceGate NGSI-v2 key-values Exemple  
Voici un exemple de SluiceGate au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### SluiceGate NGSI-v2 normalisé Exemple  
Voici un exemple de SluiceGate au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### SluiceGate NGSI-LD key-values Exemple  
Voici un exemple de SluiceGate au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SluiceGate:id:OZDE:42332657",  
    "type": "SluiceGate",  
    "address": {  
        "streetAddress": "",  
        "addressLocality": "",  
        "addressRegion": "",  
        "addressCountry": "",  
        "postalCode": "",  
        "postOfficeBoxNumber": "",  
        "areaServed": ""  
    },  
    "alternateName": "SG01 - Thivae",  
    "areaServed": "",  
    "curveDischargeCoefficient": "urn:ngsi-ld:SluiceGate:curveDischargeCoefficient:ZPPL:48418583",  
    "dataProvider": "EYDAP",  
    "dateCreated": "2021-01-13T19:49:28Z",  
    "dateModified": "2021-05-11T14:06:00Z",  
    "description": "Sluic Gate 01 - Thivae",  
    "downstreamControlPoint": "urn:ngsi-ld:SluiceGate:downstreamControlPoint:GIWE:80160975",  
    "downstreamEndControlPoint": "urn:ngsi-ld:SluiceGate:downstreamEndControlPoint:CBWI:21948924",  
    "flowType": "Submerged-Flow",  
    "gateBottomElevation": 52.3,  
    "gateDischargeCoefficient": 0.5,  
    "gateOpening": 0.5,  
    "gateWidth": 2.5,  
    "headDifference": 1.5,  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -7.578066,  
            -25.535857  
        ]  
    },  
    "name": "SG01",  
    "observedBy": "urn:ngsi-ld:SluiceGate:observedBy:ZWZM:93328711",  
    "orificeDischargeCoefficient": 0.5,  
    "owner": [  
        "urn:ngsi-ld:SluiceGate:items:LXOX:42416570",  
        "urn:ngsi-ld:SluiceGate:items:FSOL:83758025"  
    ],  
    "seeAlso": [  
        "urn:ngsi-ld:SluiceGate:items:ETJS:41829811",  
        "urn:ngsi-ld:SluiceGate:items:IKTE:29167907"  
    ],  
    "source": "",  
    "tag": "",  
    "upstreamControlPoint": "urn:ngsi-ld:SluiceGate:upstreamControlPoint:MWGU:81565938",  
    "upstreamEndControlPoint": "urn:ngsi-ld:SluiceGate:upstreamEndControlPoint:JXFD:60487647",  
    "waterDischarge": 9,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### SluiceGate NGSI-LD normalisé Exemple  
Voici un exemple de SluiceGate au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SluiceGate:id:OZDE:42332657",  
    "type": "SluiceGate",  
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
        "value": "SG01 - Thivae"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "curveDischargeCoefficient": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SluiceGate:curveDischargeCoefficient:ZPPL:48418583"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "EYDAP"  
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
    "description": {  
        "type": "Property",  
        "value": "Sluice Gate 01 - Thivae"  
    },  
    "downstreamControlPoint": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SluiceGate:downstreamControlPoint:GIWE:80160975"  
    },  
    "downstreamEndControlPoint": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SluiceGate:downstreamEndControlPoint:CBWI:21948924"  
    },  
    "flowType": {  
        "type": "Property",  
        "value": "Submerged-Flow"  
    },  
    "gateBottomElevation": {  
        "type": "Property",  
        "value": 52.3  
    },  
    "gateDischargeCoefficient": {  
        "type": "Property",  
        "value": 0.5  
    },  
    "gateOpening": {  
        "type": "Property",  
        "value": 0.5  
    },  
    "gateType": {  
        "type": "Property",  
        "value": "Sluice Gate"  
    },  
    "gateWidth": {  
        "type": "Property",  
        "value": 2.5  
    },  
    "headDifference": {  
        "type": "Property",  
        "value": 1.5  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -7.578066,  
                -25.535857  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "SG01"  
    },  
    "observedBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SluiceGate:observedBy:ZWZM:93328711"  
    },  
    "orificeDischargeCoefficient": {  
        "type": "Property",  
        "value": 0.5  
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
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "tag": {  
        "type": "Property",  
        "value": ""  
    },  
    "upstreamControlPoint": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SluiceGate:upstreamControlPoint:MWGU:81565938"  
    },  
    "upstreamEndControlPoint": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SluiceGate:upstreamEndControlPoint:JXFD:60487647"  
    },  
    "waterDischarge": {  
        "type": "Property",  
        "value": 9  
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
