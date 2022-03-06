import strawberry


from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import uvicorn
from schema import Query


schema = strawberry.Schema(Query)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


if __name__ == '__main__':
    uvicorn.run(app)
