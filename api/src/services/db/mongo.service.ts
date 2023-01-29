import { Db, MongoClient } from 'mongodb';
import { ENVIRONMENT } from 'src/environment';

export class MongoService {
  private readonly mongo: Db;

  constructor(stringConnection: string, dbName: string) {
    const mongoConnection = new MongoClient(stringConnection);
    mongoConnection.connect();
    this.mongo = mongoConnection.db(dbName);
  }

  async get<Response>(
    collection: string,
    lastRecord = false,
  ): Promise<Response> {
    const base = this.mongo.collection(collection);

    if (lastRecord) {
      return base
        .find()
        .limit(1)
        .sort({ $natural: -1 })
        .toArray() as unknown as Response;
    }

    return base.find().toArray() as unknown as Response;
  }

  static create(): MongoService {
    const dbName = 'guitar_folk';
    return new MongoService(ENVIRONMENT.MONGO_URL, dbName);
  }
}
