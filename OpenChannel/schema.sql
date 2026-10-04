/* (Beta) Export of data model OpenChannel of the subject dataModel.OpenChannelManagement for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE OpenChannel_type AS ENUM ('OpenChannel');
CREATE TABLE OpenChannel (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "downstreamNode" JSON,
  "geometry" JSON,
  "id" TEXT PRIMARY KEY,
  "location" JSON,
  "name" TEXT,
  "owner" JSON,
  "seeAlso" JSON,
  "source" TEXT,
  "tag" TEXT,
  "type" OpenChannel_type,
  "upstreamNode" JSON
);