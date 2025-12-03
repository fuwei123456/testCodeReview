import asyncio

async def noncompliant_function():  
    print("This function does nothing asynchronous")
#^[sc=1;ec=5]@-2<

async def return_from_sync_call():  
    def inner_func():
        return "result"
    return inner_func()

async def loop_function():  
    for i in range(10):
        print(i)

async def with_await():  
    result = await some_coroutine()
    return result

async def with_async_for():  
    async for item in async_iterable:
        print(item)

async def with_async_with():  
    async with async_context_manager:
        print("Inside async context")

async def non_async_with():  
    with context_manager:
        print("Inside async context")

async def with_create_task():  
    task = asyncio.create_task(some_coroutine())
    await task

async def empty_function():
    pass

async def empty_function_2():
    ...

async def empty_function_3():
    """empty for now"""
    ...

async def nested_async():  
    await some_coroutine()

    async def inner():  
        print("inner function")

    return await another_coroutine()

async def await_in_comprehension():  
    results = [await coro() for coro in coroutines]
    return results

async def nested_noncompliant():  
    def inner():
        async def deeply_nested():
            return await some_coroutine()
        return deeply_nested

    return inner()()

async def sleep_without_await():  
    asyncio.sleep(1)  

async def my_async_generator():  
    yield something()

async def async_generator_with_expression():  
    x = (yield 42)
    return x

class AsyncClass:
    async def async_method_without_await_trivial(self):  
        return self.some_attribute

    async def async_method_without_await(self):  
        do_something()
        return self.some_attribute

    async def async_method_with_await(self):  
        return await self.some_coroutine()

    @classmethod
    async def async_classmethod_without_await(cls):  
        return cls.some_value

    async def async_method_with_inner_function(self):
        async def inner_function():
            return await self.some_coroutine()
        return await inner_function()

    @abstractmethod
    async def abstract_async_method(self):  # Compliant
        raise NotImplementedError("This is an abstract method")

    @abc.abstractmethod
    async def abstract_async_method_2(self):  # Compliant
        raise NotImplementedError("This is an abstract method")

    @abc.other
    async def other_decorator_1(self):  
        raise NotImplementedError("...")

    @unknown()
    async def other_decorator_1(self):  
        raise NotImplementedError("...")

class AsyncContextManager:
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def __unknown_dunder__(self):
        # Avoid risk of FPs
        pass

    async def not_implemented_error(self):
        raise NotImplementedError("This method is not implemented")

    async def not_implemented(self):
        return NotImplemented

class AsyncIterator:
    async def __aiter__(self):
        return self

    async def __anext__(self):
        if self.should_stop():
            raise StopAsyncIteration
        return self.value

class AsyncResource:
    async def __aclose__(self):
        print("Releasing resources")

class AsyncAwaitableObject:
    async def __await__(self):
        yield "something"

    async def regular_method_without_await(self):  
        print("This is not a protocol method")

from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@app.get("/items/{item_id}")
async def read_item(item_id: int):  
    return {"item_id": item_id}

@app.post("/users/")
async def create_user(user_data: dict):  
    return {"user_id": 123, "data": user_data}

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):  
    return {"item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):  
    return {"deleted": True}


class MyClass:
    async def my_method(self):
        await something()

class MyOtherClass(MyClass):
    async def my_method(self):
        do_something()

async def async_comprehension():
    return [something async for something in async_iterable()]

async def sync_comprehension():
    return [something for something in async_iterable()]
