import { MongoService } from 'src/services/db/mongo.service';

export const PROVIDERS = {
  MONGO_SERVICE: {
    provide: 'MONGO_SERVICE',
    useFactory: MongoService.create,
  },
};
