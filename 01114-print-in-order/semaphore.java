import java.util.concurrent.Semaphore;

class Foo {
    private final Semaphore firstCompleted = new Semaphore(0);
    private final Semaphore secondCompleted = new Semaphore(0);

    public Foo() {
    }

    public void first(Runnable printFirst) throws InterruptedException {
        printFirst.run();
        
        this.firstCompleted.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        this.firstCompleted.acquire();
        printSecond.run();
        
        this.secondCompleted.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        this.secondCompleted.acquire();
        printThird.run();
    }
}
