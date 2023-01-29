import { Controller, Get, Inject } from '@nestjs/common';
import { MongoService } from '../services/db/mongo.service';
import { PROVIDERS } from '../providers';

const addMongoService = Inject(PROVIDERS.MONGO_SERVICE.provide);

@Controller('/procucts')
export class AppController {
  constructor(@addMongoService private readonly mongoService: MongoService) {}

  @Get('/guitars')
  async getProducts() {
    const collection = 'products';
    const getLastRecord = true;
    const data = await this.mongoService.get(collection, getLastRecord);
    return data;
  }
}
