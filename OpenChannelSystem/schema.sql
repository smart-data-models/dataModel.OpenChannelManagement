/* (Beta) Export of data model OpenChannelSystem of the subject dataModel.OpenChannelManagement for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE OpenChannelSystem_type AS ENUM ('OpenChannelSystem');
CREATE TABLE OpenChannelSystem (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "hasSubSystem" JSON,
  "id" TEXT PRIMARY KEY,
  "isComposedOf" JSON,
  "location" JSON,
  "mostDownstreamPoint" JSON,
  "mostUpstreamPoint" JSON,
  "name" TEXT,
  "owner" JSON,
  "seeAlso" JSON,
  "source" TEXT,
  "type" OpenChannelSystem_type
);