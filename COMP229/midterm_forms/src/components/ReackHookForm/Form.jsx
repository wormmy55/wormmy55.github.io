import { useForm } from "react-hook-form";
import "./formStyle.css";

function LoginForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
    
  const onSubmit = (data) => {
    console.log(data);
  };

return  (
  <form onSubmit={handleSubmit(onSubmit)} className="newProdForm">
  <label className="form__text">New Product</label>
  <label className="form__text">Name: </label>
  <input
    type="name"
    className="form__input"
    {...register("name", { required: true })}
  />
  {errors.name && (
    <p className="form__error">Name is required</p>
  )}

  <label className="form__text">Description: </label>
  <input
    type="description"
    className="form__input"
    {...register("description", { required: true })}
  />
  {errors.price && (
    <p className="form__error">Please input a description</p>
  )}

  <label className="form__text">Category: </label>
  <input
    type="category"
    className="form__input"
    {...register("category", { required: true })}
  />

  <label className="form__text">Quantity: </label>
  <input
    type="quantity"
    className="form__input"
    {...register("quantity", { required: true })}
  />
  {errors.price && (
    <p className="form__error">Quantity is required</p>
  )}

  <label className="form__text">Price: </label>
  <input
    type="price"
    className="form__input"
    {...register("price", { required: true })}
  />
  {errors.price && (
    <p className="form__error">Price is required</p>
  )}
  
  <button className="form__button" type="submit">
    Submit
  </button>
  <button  className="form__button" type="reset">
    Cancel
  </button>
</form>
);
}

export default LoginForm;

/*
const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="hook">
      <label className="hook__text">New Product</label>
      <input
        type="email"
        className="hook__input"
        {...register("email", { required: true, pattern: /^\S+@\S+$/i })}
      />
      {errors.email && (
        <p className="hook__error">Email is required and must be valid</p>
      )}

      <label className="hook__text">Password</label>
      <input
        type="password"
        className="hook__input"
        {...register("password", { required: true })}
      />
      {errors.password && <p className="hook__error">Password is required</p>}

      <button className="hook__button" type="submit">
        Submit
      </button>
    </form>
  );
  */