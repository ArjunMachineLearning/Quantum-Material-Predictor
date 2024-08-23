import tensorflow as tf

def custom_loss(y_true, y_pred):
    """
    Custom loss function that combines mean squared error with a penalty term.
    The penalty term is designed to enforce physical constraints by penalizing
    predictions that deviate significantly from known physical laws.
    
    Parameters:
    - y_true: Tensor, ground truth values
    - y_pred: Tensor, predicted values
    
    Returns:
    - Tensor, the computed loss value
    """
    # Mean squared error loss
    mse_loss = tf.reduce_mean(tf.square(y_true - y_pred))
    
    # Penalty term to enforce physical constraints
    penalty = tf.reduce_mean(tf.square(tf.maximum(0.0, y_pred - y_true)))
    
    # Total loss: mean squared error plus penalty
    total_loss = mse_loss + penalty
    
    return total_loss

# Optional: To verify if the loss function is working as intended
if __name__ == "__main__":
    # Example tensors for testing
    y_true = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
    y_pred = tf.constant([1.5, 2.5, 3.5], dtype=tf.float32)
    
    # Calculate the custom loss
    loss = custom_loss(y_true, y_pred)
    print(f"Custom Loss: {loss.numpy()}")
