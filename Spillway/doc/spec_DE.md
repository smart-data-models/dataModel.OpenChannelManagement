<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Spillway  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.OpenChannelManagement/blob/master/Spillway/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen Überlaufs für die Systemmanagementdomäne Rohwasser (offene Kanäle). Die Hochwasserentlastungsanlage stellt ein Objekt des Typs Kreuzung dar, das die Wasserabgabe aus einem Damm oder einer stromabwärts gelegenen Regulierungsstruktur steuert.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `apronElevation[number]`: Die Höhe an der Unterseite des Hochwasserentlastungsbauwerks (P), unmittelbar stromaufwärts der Hochwasserentlastung  - `apronLength[number]`: Die Gesamtlänge der Überlaufsohle  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `controlCrossSection[*]`: Eine Beziehung, die die ID einer Entität vom Typ Querschnitt angibt, die den Querschnitt angibt, der den Durchfluss über die Hochwasserentlastungsanlage steuert  - `crestElevation[number]`: Die Scheitelhöhe der Hochwasserentlastungsanlage. Nur erforderlich für "Broad-Crested", "Ogee" und "Sharp-Crested".  - `crestLength[number]`: Die Länge der Überlaufrinne entspricht der Gesamtlänge, durch die das Wasser fließt. Nur erforderlich für "Broad-Crested", "Ogee" und "Sharp-Crested".  - `curveDesignDischargeCoefficient[*]`: Die URI einer OpenChannelCurve-Entität, die den Bemessungsabflusskoeffizienten (Co) als Funktion der Vorfeldhöhe über der Bemessungsfallhöhe (Co-P/Ho) darstellt  - `curveDischargeCoefficient[*]`: Die URI einer OpenChannelCurve-Entität, die den Abflusskoeffizienten (C) in Abhängigkeit von der Oberwasserhöhe (H) und der Überlaufgeometrie darstellt. Zum Beispiel: Abflussbeiwert als Funktion der Oberwasserhöhe über der Überlaufbreite (C-H/L) oder C/Co-H/Ho  - `curveElevationDischarge[*]`: Die URI einer OpenChannelCurve-Entität, die den Abfluss (Q) als Funktion der Wasserhöhe (H) darstellt  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `designDischarge[number]`: Der Bemessungsabfluss (Qo) der Hochwasserentlastungsanlage  - `designDischargeCoefficient[number]`: Der Abflusskoeffizient (Co) für Energieverluste für den Bemessungsabfluss (Ho)  - `designHead[number]`: Die gesamte stromaufwärts gerichtete Fallhöhe, für die der Überlauf ausgelegt ist (Ho), für "Ogee Spillway  - `dischargeCoefficient[number]`: Der Abflusskoeffizient für die Energieverluste bei Eintritt, Durchfluss und Austritt des Wassers aus der Hochwasserentlastungsanlage  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `maxFloodElevation[number]`: Die maximale Höhe des Wassers, das die Hochwasserentlastungsanlage passieren kann  - `name[string]`: Der Name dieses Artikels  - `numberAbutments[number]`: Die Anzahl der Widerlager eines Ogee-Überlaufs. Nur für den Typ 'Ogee'.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `spillwayType[string]`: Der Typ der Hochwasserentlastungsanlage. Im Falle von "Specified Spillway" ist nur die Kurve "Elevation - discharge" erforderlich. Enum:'Broad-Crested, Ogee, Sharp-Crested, Specified Spillway'  - `spillwayWidth[number]`: Die Breite des Überlaufs (m). Nur für den Typ "Broad-Crested".  - `tag[string]`: Eine optionale Textzeichenfolge, die zur Qualifizierung einer Position verwendet wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-Entitätstyp. Es muss Spillway sein  - `waterDischarge[number]`: Der Abfluss über die Hochwasserentlastung (Q)  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `location`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Spillway:    
  description: 'This entity contains a harmonised description for a generic Spillway made for Raw-Water (Open Channels) System Management domain. Spillway represents a junction-type object, controlling the release of water from a dam or regulation structure downstream.'    
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
    apronElevation:    
      description: 'The elevation at the bottom of the ogee spillway structure (P), just upstream of the spillway'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    apronLength:    
      description: The total length of the spillway bottom    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    controlCrossSection:    
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
      description: 'A relationship indicating the ID of an entity of type Cross Section, indicating the cross section that controls the flow over the Spillway'    
      x-ngsi:    
        type: Relationship    
    crestElevation:    
      description: 'The crest elevation of the Spillway. Required only for ''Broad-Crested'', ''Ogee'' and ''Sharp-Crested'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    crestLength:    
      description: 'The length of the Spillway equals to the total length through which water passes. Required only for ''Broad-Crested'', ''Ogee'' and ''Sharp-Crested'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    curveDesignDischargeCoefficient:    
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
      description: The URI of an OpenChannelCurve entity that represents the design discharge coefficient (Co) as a function of apron Elevation over design upstream head (Co-P/Ho)    
      x-ngsi:    
        type: Relationship    
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
      description: 'The URI of an OpenChannelCurve entity that represents the discharge coefficient (C) as a function of upstream head (H) and spillway geometry. For instance, discharge coefficient as a function of upstream head over spillway width (C-H/L), or C/Co-H/Ho'    
      x-ngsi:    
        type: Relationship    
    curveElevationDischarge:    
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
      description: The URI of an OpenChannelCurve entity that represents discharge (Q) as a function of water elevation (H)    
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
    designDischarge:    
      description: The design discharge (Qo) of the Spillway    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: ' m^3/s'    
    designDischargeCoefficient:    
      description: The discharge coefficient (Co) for energy losses for the design discharge (Ho)    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    designHead:    
      description: The total upstream energy head for which the spillway is designed (Ho) for 'Ogee Spillway'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    dischargeCoefficient:    
      description: 'The discharge coefficient for energy losses as water enters, flows and exits the spillway'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: m^0.5/s    
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
    maxFloodElevation:    
      description: The maximum elevation of water that can pass the spillway    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    numberAbutments:    
      description: The number of abutments of an ogee spillway. Only for 'Ogee' type    
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
    spillwayType:    
      description: 'The type of the spillway. In the case of “Specified Spillway”, only “Elevation – discharge” curve is required. Enum:''Broad-Crested, Ogee, Sharp-Crested, Specified Spillway'''    
      enum:    
        - Broad-Crested    
        - Ogee    
        - Sharp-Crested    
        - Specified Spillway    
      type: string    
      x-ngsi:    
        type: Property    
    spillwayWidth:    
      description: The width of the spillway (m). Only for 'Broad-Crested' type    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: meters    
    tag:    
      description: An optional text string used to qualify an item    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity Type. It has to be Spillway    
      enum:    
        - Spillway    
      type: string    
      x-ngsi:    
        type: Property    
    waterDischarge:    
      description: The discharge over the spillway (Q)    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: ' m^3/s'    
  required:    
    - id    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OpenChannelManagement/blob/master/Spillway/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.OpenChannelManagement/Spillway/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### Hochwasserschutz NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Spillway im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Spillway:id:FFPG:06271993",  
  "type": "Spillway",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      60.3603485,  
      -129.682253  
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
  "dateCreated": "2020-10-12T04:27:47Z",  
  "dateModified": "2021-09-26T16:22:05Z",  
  "source": "",  
  "name": "SP01",  
  "alternateName": "SP01 - Thivae",  
  "description": "Spillway 01 - Thivae",  
  "dataProvider": "EYDAP",  
  "owner": [  
    "urn:ngsi-ld:Spillway:items:OFPV:04640010",  
    "urn:ngsi-ld:Spillway:items:BFAT:33357858"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Spillway:items:VLIF:47226224",  
    "urn:ngsi-ld:Spillway:items:BDSZ:68275691"  
  ],  
  "tag": "",  
  "spillwayType": "Ogee",  
  "crestElevation": 26.4,  
  "crestLength": 5,  
  "spillwayWidth": 5,  
  "numberAbutments": 2,  
  "apronElevation": 22,  
  "apronLength": 5,  
  "dischargeCoefficient": 5,  
  "designHead": 30.4,  
  "designDischarge": 20,  
  "designDischargeCoefficient": 0.4,  
  "maxFloodElevation": 4,  
  "waterDischarge": 9,  
  "controlCrossSection": "urn:ngsi-ld:Spillway:controlCrossSection:JXFD:60487647",  
  "curveElevationDischarge": "urn:ngsi-ld:Spillway:curveElevationDischarge:CBWI:21948924",  
  "curveDischargeCoefficient": "urn:ngsi-ld:Spillway:curveDischargeCoefficient:MWGU:81565938",  
  "curveDesignDischargeCoefficient": "urn:ngsi-ld:Spillway:curveDesignDischargeCoefficient:GIWE:80160975"  
}  
```  
</details>  
#### Hochwasserentlastung NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Spillway im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Spillway:id:FFPG:06271993",  
  "type": "Spillway",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        60.3603485,  
        -129.682253  
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
  "dateCreated":{  
      "type": "DateTime",  
      "value": "2020-10-12T04:27:47Z"  
  },  
  "dateModified": {  
      "type": "DateTime",  
      "value": "2021-09-26T16:22:05Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "SP01"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "SP01 - Thivae"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Spillway 01 - Thivae"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "EYDAP"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Spillway:items:OFPV:04640010",  
      "urn:ngsi-ld:Spillway:items:BFAT:33357858"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:Spillway:items:VLIF:47226224",  
      "urn:ngsi-ld:Spillway:items:BDSZ:68275691"  
    ]  
  },  
  "tag": {  
    "type": "Text",  
    "value": ""  
  },  
  "spillwayType": {  
    "type": "Text",  
    "value": "Ogee"  
  },  
  "crestElevation": {  
    "type": "Number",  
    "value": 26.4  
  },  
  "crestLength": {  
    "type": "Number",  
    "value": 5  
  },  
  "spillwayWidth": {  
    "type": "Number",  
    "value": 5  
  },  
  "numberAbutments": {  
    "type": "Number",  
    "value": 2  
  },  
  "apronElevation": {  
    "type": "Number",  
    "value": 22  
  },  
  "apronLength": {  
    "type": "Number",  
    "value": 5  
  },  
  "dischargeCoefficient": {  
    "type": "Number",  
    "value": 5  
  },  
  "designHead": {  
    "type": "Number",  
    "value": 30.4  
  },  
  "designDischarge": {  
    "type": "Number",  
    "value": 20  
  },  
  "designDischargeCoefficient": {  
    "type": "Number",  
    "value": 0.4  
  },  
  "maxFloodElevation": {  
    "type": "Number",  
    "value": 4  
  },  
  "waterDischarge": {  
    "type": "Number",  
    "value": 9  
  },    
  "controlCrossSection": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Spillway:controlCrossSection:JXFD:60487647"  
  },  
  "curveElevationDischarge": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Spillway:curveElevationDischarge:CBWI:21948924"  
  },  
  "curveDischargeCoefficient": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Spillway:curveDischargeCoefficient:MWGU:81565938"  
  },  
  "curveDesignDischargeCoefficient": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Spillway:curveDesignDischargeCoefficient:GIWE:80160975"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### Hochwasserentlastung NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Spillway im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Spillway:id:FFPG:06271993",  
    "type": "Spillway",  
    "address": {  
        "streetAddress": "",  
        "addressLocality": "",  
        "addressRegion": "",  
        "addressCountry": "",  
        "postalCode": "",  
        "postOfficeBoxNumber": "",  
        "areaServed": ""  
    },  
    "alternateName": "SP01 - Thivae",  
    "apronElevation": 22,  
    "apronLength": 5,  
    "areaServed": "",  
    "controlCrossSection": "urn:ngsi-ld:Spillway:controlCrossSection:JXFD:60487647",  
    "crestElevation": 26.4,  
    "crestLength": 5,  
    "curveDesignDischargeCoefficient": "urn:ngsi-ld:Spillway:curveDesignDischargeCoefficient:GIWE:80160975",  
    "curveDischargeCoefficient": "urn:ngsi-ld:Spillway:curveDischargeCoefficient:MWGU:81565938",  
    "curveElevationDischarge": "urn:ngsi-ld:Spillway:curveElevationDischarge:CBWI:21948924",  
    "dataProvider": "EYDAP",  
    "dateCreated": "2020-10-12T04:27:47Z",  
    "dateModified": "2021-09-26T16:22:05Z",  
    "description": "Spillway 01 - Thivae",  
    "designDischarge": 20,  
    "designDischargeCoefficient": 0.4,  
    "designHead": 30.4,  
    "dischargeCoefficient": 5,  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            60.3603485,  
            -129.682253  
        ]  
    },  
    "maxFloodElevation": 4,  
    "name": "SP01",  
    "numberAbutments": 2,  
    "owner": [  
        "urn:ngsi-ld:Spillway:items:OFPV:04640010",  
        "urn:ngsi-ld:Spillway:items:BFAT:33357858"  
    ],  
    "seeAlso": [  
        "urn:ngsi-ld:Spillway:items:VLIF:47226224",  
        "urn:ngsi-ld:Spillway:items:BDSZ:68275691"  
    ],  
    "source": "",  
    "spillwayType": "Ogee",  
    "spillwayWidth": 5,  
    "tag": "",  
    "waterDischarge": 9,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OpenChannelManagement/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Hochwasserentlastung NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Überlauf im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Spillway:id:FFPG:06271993",  
    "type": "Spillway",  
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
        "value": "SP01 - Thivae"  
    },  
    "apronElevation": {  
        "type": "Property",  
        "value": 22  
    },  
    "apronLength": {  
        "type": "Property",  
        "value": 5  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": ""  
    },  
    "controlCrossSection": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Spillway:controlCrossSection:JXFD:60487647"  
    },  
    "crestElevation": {  
        "type": "Property",  
        "value": 26.4  
    },  
    "crestLength": {  
        "type": "Property",  
        "value": 5  
    },  
    "curveDesignDischargeCoefficient": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Spillway:curveDesignDischargeCoefficient:GIWE:80160975"  
    },  
    "curveDischargeCoefficient": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Spillway:curveDischargeCoefficient:MWGU:81565938"  
    },  
    "curveElevationDischarge": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Spillway:curveElevationDischarge:CBWI:21948924"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "EYDAP"  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-10-12T04:27:47Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-09-26T16:22:05Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Spillway 01 - Thivae"  
    },  
    "designDischarge": {  
        "type": "Property",  
        "value": 20  
    },  
    "designDischargeCoefficient": {  
        "type": "Property",  
        "value": 0.4  
    },  
    "designHead": {  
        "type": "Property",  
        "value": 30.4  
    },  
    "dischargeCoefficient": {  
        "type": "Property",  
        "value": 5  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                60.3603485,  
                -129.682253  
            ]  
        }  
    },  
    "maxFloodElevation": {  
        "type": "Property",  
        "value": 4  
    },  
    "name": {  
        "type": "Property",  
        "value": "SP01"  
    },  
    "numberAbutments": {  
        "type": "Property",  
        "value": 2  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:Spillway:items:OFPV:04640010",  
            "urn:ngsi-ld:Spillway:items:BFAT:33357858"  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:Spillway:items:VLIF:47226224",  
            "urn:ngsi-ld:Spillway:items:BDSZ:68275691"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "spillwayType": {  
        "type": "Property",  
        "value": "Ogee"  
    },  
    "spillwayWidth": {  
        "type": "Property",  
        "value": 5  
    },  
    "tag": {  
        "type": "Property",  
        "value": ""  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
